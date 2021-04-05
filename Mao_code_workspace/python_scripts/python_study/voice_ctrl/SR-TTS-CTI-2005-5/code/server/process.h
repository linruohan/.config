#include <stdlib.h>
#include <winsock2.h>
#include "DefTypes.h"
#include <string.h>

#include "LoginMessage.h"
#include "OnLIneInfoQueue.h"
#include "OnlineInfoItem.h"
#include "SerFrame.h"
/////////////////////////////////////////////////////////////////////////////

#include <afxdb.h>
extern	CDatabase database;
extern	bool quit;
extern  char   RecvBuf[DEFAULT_BUFFER_LENGTH];
extern COnLIneInfoQueue  OnLIneInfoQueue;
extern	SOCKET ListenSock;
///////////			声明外部变量		/////////////////
////////////////////////////////////////
DWORD WINAPI ProcessLoginThread(LPVOID lpParam);
DWORD WINAPI ProcessLandingThread(LPVOID lpParam);
DWORD WINAPI ProcessUserQuitThread(LPVOID lpParam);
int sendto_onlineinfo(SOCKET s, SOCKADDR *TOAddr, int TOLen);
int sendto_onlineNotify(SOCKET SockForNotify,SOCKADDR *TOAddr, int TOLen,COnlineInfoItem item);
void GetType(char *Source ,int *Type);

DWORD WINAPI ProcessThread(LPVOID lpParam)
{
	SOCKET        sock=(SOCKET)lpParam;
    int           ret;
    SOCKADDR_IN   sender;
    int           dwSenderSize;
    dwSenderSize = sizeof(sender);
	int           Type=0;
	HANDLE        hThread;
	DWORD         dwThreadId;
	ioctlsocket(sock , FIONBIO, 0 );
	while(!quit)
	{
		ret = recvfrom(sock, RecvBuf, DEFAULT_BUFFER_LENGTH, 0, 
                   	       (SOCKADDR *)&sender, &dwSenderSize);
                   	  
        GetType(RecvBuf,&Type);
        if(Type==USER_LOGIN_MESSAGE)
        {
            hThread = ::CreateThread(NULL, 0, ProcessLoginThread, 
                                     (LPVOID)&sender, 0, &dwThreadId);
			CloseHandle(hThread);
		}
		if(Type==USER_LANDING_MESSAGE)
		{
			hThread = ::CreateThread(NULL, 0, ProcessLandingThread, 
                                     (LPVOID)&sender, 0, &dwThreadId);
			CloseHandle(hThread);
		}	
		if(Type==USER_QUIT_MESSAGE)
		{
			hThread = ::CreateThread(NULL, 0, ProcessUserQuitThread, 
                                     (LPVOID)&sender, 0, &dwThreadId);
			CloseHandle(hThread);
		}			
	}
	return 0;
}
void GetType(char *Source ,int *Type)
{
	char   TypeBuf[5];//有4位是数字，后一位是'\0';
	int    i;
	for(i=0;i<4;i++)
	TypeBuf[i]= Source[i];
	TypeBuf[4]='\0';
	*Type=atoi(TypeBuf);
}

	
DWORD WINAPI ProcessLoginThread(LPVOID lpParam)
{
	SOCKADDR_IN    *clientaddr =(SOCKADDR_IN  *)lpParam;////////客户端的地址；
	SOCKADDR_IN     NewClientAddr;
	
	
	char NameBuf[25],Password[25];
	int  HeadID;
	TRACE("\nRecvBuff is %s,form port %d\n",RecvBuf,ntohs(clientaddr->sin_port));
	TRACE("\nfromip is %s\n",inet_ntoa(clientaddr->sin_addr));	
	CLoginMessage LoginMessage(RecvBuf);
	
	NewClientAddr.sin_port=htons((short)ntohs(clientaddr->sin_port));//找到客户端的监听端口并修改地址;
    NewClientAddr.sin_addr=clientaddr->sin_addr;
    NewClientAddr.sin_family=AF_INET;

	TRACE("\nclientport is %d\n",ntohs(clientaddr->sin_port));
	strcpy(NameBuf, LoginMessage.GetLoginName());
	strcpy(Password, LoginMessage.GetLoginPassword());
	HeadID=LoginMessage.GetLoginHeadID();
	CString strSql;			//sql语句
	
	CRecordset recordset;
	recordset.m_pDatabase=&database;
	
	strSql.Format("select * from UserInfo where UserName='%s'",NameBuf);
	recordset.Open(AFX_DB_USE_DEFAULT_TYPE,strSql);	//按输入的用户名查询，执行sql语句
	
	if(recordset.GetRecordCount()>0)	//如果查询纪录为空
	{
		TRACE("用户已经存在\n");
		CString error("0");
		sendto(ListenSock, error, error.GetLength(), 0,(SOCKADDR *) &NewClientAddr, sizeof(NewClientAddr));//0  为注册失败.
		return 0;
	}
	TRACE("\nNameBuf is %s,Password is %s,HeadID is %d\n" , NameBuf , Password , HeadID);
	strSql.Empty();
	strSql.Format("insert into UserInfo values('%s','%s','%d')",NameBuf,
		            Password,HeadID);

	database.ExecuteSQL(strSql);
	CString ok("1");
	sendto(ListenSock, ok, ok.GetLength(), 0,(SOCKADDR *) &NewClientAddr, sizeof(NewClientAddr));//1  为成功注册
	return 0;
}
DWORD WINAPI ProcessLandingThread(LPVOID lpParam)
{
	SOCKADDR_IN    *clientaddr =(SOCKADDR_IN  *)lpParam;////////客户端的地址；
	SOCKADDR_IN     NewClientAddr;
	
	TRACE("\nform port %d\n",ntohs(clientaddr->sin_port));
	char NameBuf[25],Password[25];
	int HeadID;
	CLoginMessage LoginMessage(RecvBuf);//注册报文和登陆报文的格式是一样的。
	
	NewClientAddr.sin_port=htons((short)ntohs(clientaddr->sin_port));//找到客户端的监听端口并修改地址;
    NewClientAddr.sin_addr=clientaddr->sin_addr;
    NewClientAddr.sin_family=AF_INET;

	TRACE("\nclientport is %d\n",ntohs(clientaddr->sin_port));
	strcpy(NameBuf, LoginMessage.GetLoginName());
	strcpy(Password, LoginMessage.GetLoginPassword());
	CString strSql;			//sql语句
	
	CRecordset recordset;
	recordset.m_pDatabase=&database;
	strSql.Format("select * from UserInfo where UserName='%s'",NameBuf);
	recordset.Open(AFX_DB_USE_DEFAULT_TYPE,strSql);	//按输入的用户名查询，执行sql语句
	
	int pos;
	if(OnLIneInfoQueue.SearchItemByUserName(NameBuf,&pos))
	{
		TRACE("该用户已经登陆\n");
		CString error("3");
		sendto(ListenSock, error, error.GetLength(), 0,(SOCKADDR *) &NewClientAddr, sizeof(NewClientAddr));//0  为注册失败.
		return 0;
	}
	if(recordset.GetRecordCount()==0)	//如果查询纪录为空
	{
		TRACE("\n无此用户\n");
		CString error("1");//无此用户
		sendto(ListenSock, error, error.GetLength(), 0,(SOCKADDR *) &NewClientAddr, sizeof(NewClientAddr));
		return 0;
	}
	CDBVariant varValue;	//变体类型，存放
	recordset.GetFieldValue("Password",varValue);	
	if(strcmp(Password,varValue.m_pstring->GetBuffer(1))==0)
	{
		sendto_onlineinfo(ListenSock, (SOCKADDR *) &NewClientAddr, sizeof(NewClientAddr));
		//先发送在线者的信息，然后在把这个登陆的用户的信息加入
		//在线信息队列，这样可以解决把自己的信息在发回去的问题。
		
		recordset.GetFieldValue("HeadId",varValue);
		HeadID=varValue.m_iVal;
		COnlineInfoItem item(ntohs(clientaddr->sin_port),
							 HeadID,
							 inet_ntoa(clientaddr->sin_addr),
							 NameBuf);
		for(int i=0;i<OnLIneInfoQueue.UserNumber;i++)
		{
			SOCKADDR_IN     Addr;
			Addr.sin_port=htons((short)OnLIneInfoQueue[i].GetListenPort());
    		Addr.sin_addr.s_addr = inet_addr((LPSTR)(LPCTSTR)OnLIneInfoQueue[i].GetIP());
    		Addr.sin_family=AF_INET;
    		sendto_onlineNotify(ListenSock,(SOCKADDR *) &Addr, sizeof(Addr),item);
    	}
    	OnLIneInfoQueue.AddItem(item);					 
		TRACE("\n成功登陆\n");
	}	
	
	else 
	{
		TRACE("\n密码错误\n");
		CString error("2");//密码错误
		sendto(ListenSock, error, error.GetLength(), 0,(SOCKADDR *) &NewClientAddr, sizeof(NewClientAddr));
		return 0;
	}
	return 0;
}
int sendto_onlineinfo(SOCKET s, SOCKADDR *TOAddr, int TOLen)
{
	/////先封装报文格式：回应登陆成功报文/////////////////////////////
	char SendBuf[4096];
	char sIPBuf[17],sUserNameBuf[15],sPortBuf[6],sHeadIDBuf[3],
		 sIPLen[3],sUsernameLen[3],sUserNumber[4];//比报文格式多出一个字符用来存'\0';
	int  iIPLen,iUsernameLen,iPort,iHeadID;
	strcpy(SendBuf,"0000");
	if(OnLIneInfoQueue.UserNumber==0)
	{
		TRACE("\nonlineinfo is %s\n",SendBuf);
		return sendto(s, SendBuf, strlen(SendBuf), 0,TOAddr, TOLen);//发送4个0，对应回应登陆成功报文。
	}
	else
	{
		for(int i=0;i<OnLIneInfoQueue.UserNumber;i++)
		{
			strcpy(sIPBuf,OnLIneInfoQueue[i].GetIP());
			
			iIPLen=strlen(sIPBuf);
			sprintf(sIPLen,"%d",iIPLen );
			if(iIPLen<10)
			sprintf(sIPLen,"0%d",iIPLen );
			strcat(SendBuf,sIPLen);//处理IP长度字段
			
			while(iIPLen!=16)
			{
				strcat(sIPBuf,"0");
				iIPLen=strlen(sIPBuf);
			}
			strcat(SendBuf,sIPBuf);//处理IP字段
			
			strcpy(sUserNameBuf,OnLIneInfoQueue[i].GetUserName());
			iUsernameLen=strlen(sUserNameBuf);
			sprintf(sUsernameLen,"%d",iUsernameLen );
			if(iUsernameLen<10)
			sprintf(sUsernameLen,"0%d",iUsernameLen );
			strcat(SendBuf,sUsernameLen);//处理用户名长度字段
			
			while(iUsernameLen!=14)
			{
				strcat(sUserNameBuf,"0");
				iUsernameLen=strlen(sUserNameBuf);
			}
			strcat(SendBuf,sUserNameBuf);//处理用户名字段
			
			iPort=OnLIneInfoQueue[i].GetListenPort();
			sprintf(sPortBuf,"%d",iPort);
			if(strlen(sPortBuf)==4)
			sprintf(sPortBuf,"0%d",iPort);
			strcat(SendBuf,sPortBuf);//处理监听端口字段
			
			
			iHeadID=OnLIneInfoQueue[i].GetHeadID();
			sprintf(sHeadIDBuf,"%d",iHeadID);
			if(strlen(sHeadIDBuf)==1)
			sprintf(sHeadIDBuf,"0%d",iHeadID);
			strcat(SendBuf,sHeadIDBuf);//处理头像代码字段
		}
	}
	if(OnLIneInfoQueue.UserNumber>=100)//3位数
	sprintf(sUserNumber,"%d",OnLIneInfoQueue.UserNumber);
	if((OnLIneInfoQueue.UserNumber<100)&&(OnLIneInfoQueue.UserNumber>=10))//2位数
	sprintf(sUserNumber,"0%d",OnLIneInfoQueue.UserNumber);
	if(OnLIneInfoQueue.UserNumber<10)//1位数
	sprintf(sUserNumber,"00%d",OnLIneInfoQueue.UserNumber);
	
	SendBuf[1]=sUserNumber[0];
	SendBuf[2]=sUserNumber[1];
	SendBuf[3]=sUserNumber[2];//修改报文格式中的在线用户个数字段
	TRACE("\nonlineinfo is %s\n",SendBuf);
	return sendto(s,SendBuf,strlen(SendBuf), 0,TOAddr, TOLen);
}   

int sendto_onlineNotify(SOCKET SockForNotify,SOCKADDR *TOAddr, int TOLen,COnlineInfoItem item)
{
	char SendBuf[100];
	char sIPBuf[17],sUserNameBuf[15],sPortBuf[6],sHeadIDBuf[3],
		 sIPLen[3],sUsernameLen[3];//比报文格式多出一个字符用来存'\0';
	int  iIPLen,iUsernameLen,iPort,iHeadID;
	strcpy(SendBuf,"3003");
	strcpy(sIPBuf,item.GetIP());
			
	iIPLen=strlen(sIPBuf);
	sprintf(sIPLen,"%d",iIPLen );
	if(iIPLen<10)
	sprintf(sIPLen,"0%d",iIPLen );
	strcat(SendBuf,sIPLen);//处理IP长度字段
			
	while(iIPLen!=16)
	{
		strcat(sIPBuf,"0");
		iIPLen=strlen(sIPBuf);
	}
	strcat(SendBuf,sIPBuf);//处理IP字段
			
	strcpy(sUserNameBuf,item.GetUserName());
    iUsernameLen=strlen(sUserNameBuf);
	sprintf(sUsernameLen,"%d",iUsernameLen );
	if(iUsernameLen<10)
	sprintf(sUsernameLen,"0%d",iUsernameLen );
	strcat(SendBuf,sUsernameLen);//处理用户名长度字段
			
	while(iUsernameLen!=14)
	{
		strcat(sUserNameBuf,"0");
		iUsernameLen=strlen(sUserNameBuf);
	}
	strcat(SendBuf,sUserNameBuf);//处理用户名字段
			
	iPort=item.GetListenPort();
	sprintf(sPortBuf,"%d",iPort);
	if(strlen(sPortBuf)==4)
	sprintf(sPortBuf,"0%d",iPort);
	strcat(SendBuf,sPortBuf);//处理监听端口字段
			
			
	iHeadID=item.GetHeadID();
	sprintf(sHeadIDBuf,"%d",iHeadID);
	if(strlen(sHeadIDBuf)==1)
	sprintf(sHeadIDBuf,"0%d",iHeadID);
	strcat(SendBuf,sHeadIDBuf);//处理头像代码字段
	TRACE("\nonlineNotify sendbuf is %s\n",SendBuf);
	return sendto(SockForNotify,SendBuf,strlen(SendBuf), 0,TOAddr, TOLen);
}
DWORD WINAPI ProcessUserQuitThread(LPVOID lpParam)
{
	char sRecvBuf[100];
	strcpy(sRecvBuf,RecvBuf);
	char lenbuf[3];//有2位是数字，后一位是'\0';
	int len,i;
	char sUserName[25];
	for(i=4;i<6;i++)
	lenbuf[i-4]= sRecvBuf[i];
	lenbuf[2]='\0';
	len=atoi(lenbuf);
	
	for(i=6;i<6+len;i++)
	sUserName[i-6]=sRecvBuf[i];
	sUserName[i-6]='\0';
	int pos;
	TRACE("%s下线了",sUserName);
	OnLIneInfoQueue.SearchItemByUserName(sUserName,&pos);
	OnLIneInfoQueue.PrintQueue();
	OnLIneInfoQueue.DeleteItem(pos);
	OnLIneInfoQueue.PrintQueue();
	char sendbuf[100];
	sendbuf[0]='\0';
    int   ret,dwLength;
    
    strcat(sendbuf,"3005");
    CString str;
	str.Format("%d",strlen(sUserName));
	if(strlen(sUserName)<10)
	str.Format("0%d",strlen(sUserName));
	str+=sUserName;
	strcat(sendbuf,str);
	TRACE("下线通知 sendbuf is %s",sendbuf);
	dwLength=strlen(sendbuf);
    
	
	for(i=0;i<OnLIneInfoQueue.UserNumber;i++)
	{
		SOCKADDR_IN     Addr;
		Addr.sin_port=htons((short)OnLIneInfoQueue[i].GetListenPort());
    	Addr.sin_addr.s_addr = inet_addr((LPSTR)(LPCTSTR)OnLIneInfoQueue[i].GetIP());
    	Addr.sin_family=AF_INET;
    	ret = sendto(ListenSock, sendbuf, dwLength, 0, 
                 	(SOCKADDR *)&Addr, sizeof(Addr));
    }
 	return 0;
}
