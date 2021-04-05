// LoginMessage.cpp: implementation of the CLoginMessage class.
//
//////////////////////////////////////////////////////////////////////

#include <stdlib.h>
#include <string.h>
#include "stdafx.h"
#include "LoginMessage.h"

//////////////////////////////////////////////////////////////////////
// Construction/Destruction
//////////////////////////////////////////////////////////////////////



CLoginMessage::CLoginMessage(char *RecvBuf)
{
	    strcpy(LoginMessage,RecvBuf);
}
int  CLoginMessage::GetLoginNameLen()
{
	int i ,len ;
	char lenbuf[3];//有2位是数字，后一位是'\0';
	
	for(i=4;i<6;i++)
	lenbuf[i-4]= LoginMessage[i];
	lenbuf[2]='\0';
	len=atoi(lenbuf);
	return len;
}   
int  CLoginMessage::GetLoginPasswordLen()
{
	int i, LoginNamelen, LoginPasswordlen ;
	char lenbuf[3];//有2位是数字，后一位是'\0';
	LoginNamelen=GetLoginNameLen();
	
	for(i=6+LoginNamelen;i<8+LoginNamelen;i++)
	lenbuf[i-6-LoginNamelen]= LoginMessage[i];
	lenbuf[2]='\0';
	LoginPasswordlen=atoi(lenbuf);
	return LoginPasswordlen;
}
char* CLoginMessage::GetLoginName()
{
	int LoginNamelen  = GetLoginNameLen();
	for(int i=6;i<LoginNamelen+6;i++)
	LoginName[i-6]=LoginMessage[i];
	LoginName[i-6]='\0'; 
	return LoginName;
}

char* CLoginMessage::GetLoginPassword()
{
	int   LoginNamelen     = GetLoginNameLen();
	int   LoginPasswordlen = GetLoginPasswordLen() ;
	for(int i=8+LoginNamelen;i<8+LoginPasswordlen+LoginNamelen;i++)
	LoginPassword[i-8-LoginNamelen]=LoginMessage[i];
	LoginPassword[i-8-LoginNamelen]='\0';
	return LoginPassword;
}
int   CLoginMessage::GetLoginHeadID()
{
	int   LoginNamelen     = GetLoginNameLen();
	int   LoginPasswordlen = GetLoginPasswordLen() ;
	char lenbuf[3];
	int  headID;
	int  headbegin=8+LoginNamelen+LoginPasswordlen;
	for(int i=headbegin;i<headbegin+2;i++)
	lenbuf[i-headbegin]= LoginMessage[i];
	lenbuf[2]='\0';
	headID=atoi(lenbuf);
	return headID;
}
int   CLoginMessage::GetClientPort()
{
	int messagelen;
	char lenbuf[6];
	messagelen=strlen(LoginMessage);
	for(int i=messagelen-5;i<=messagelen;i++)
	lenbuf[i-messagelen+5]=LoginMessage[i];
	lenbuf[5]='\0';
	return atoi(lenbuf);
}