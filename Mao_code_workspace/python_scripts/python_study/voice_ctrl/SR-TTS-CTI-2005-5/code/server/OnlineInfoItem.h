// OnlineInfoItem.h: interface for the COnlineInfoItem class.
//
//////////////////////////////////////////////////////////////////////

#if !defined(AFX_ONLINEINFOITEM_H__F467D866_2E7F_4148_9604_DD33B8C62A2C__INCLUDED_)
#define AFX_ONLINEINFOITEM_H__F467D866_2E7F_4148_9604_DD33B8C62A2C__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

class COnlineInfoItem  
{
public:
	COnlineInfoItem();
	COnlineInfoItem(int Port,int HeadId,CString IP,CString Username);
	virtual ~COnlineInfoItem();
	
	COnlineInfoItem *next;//¡¥±Ì÷∏’Î
	
	void SetListenPort(int port);
	void SetHeadID(int ID);
	void SetIP(CString IP);
	void SetUserName(CString UserName);
	
	int GetListenPort();
	int GetHeadID();
	CString GetIP();
	CString GetUserName();
	
	COnlineInfoItem& operator=(COnlineInfoItem item);
private:
    int      iListenPort;
    int      iHeadID;
    CString  sIP;
    CString  sUserName;

};

#endif // !defined(AFX_ONLINEINFOITEM_H__F467D866_2E7F_4148_9604_DD33B8C62A2C__INCLUDED_)
