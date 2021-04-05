// OnlineInfoItem.cpp: implementation of the COnlineInfoItem class.
//
//////////////////////////////////////////////////////////////////////

#include "stdafx.h"
#include "SerFrame.h"
#include "OnlineInfoItem.h"

#ifdef _DEBUG
#undef THIS_FILE
static char THIS_FILE[]=__FILE__;
#define new DEBUG_NEW
#endif

//////////////////////////////////////////////////////////////////////
// Construction/Destruction
//////////////////////////////////////////////////////////////////////
COnlineInfoItem& COnlineInfoItem::operator=(COnlineInfoItem item)
{
	iListenPort=item.GetListenPort();
	iHeadID=item.GetHeadID();
    sIP=item.GetIP();
    sUserName=item.GetUserName();
    next=NULL;
	return *this;
}

void COnlineInfoItem::SetListenPort(int port)
{
	iListenPort=port;
}
void COnlineInfoItem::SetHeadID(int ID)
{
	iHeadID=ID;
}
void COnlineInfoItem::SetIP(CString IP)
{
	sIP=IP;
}
void COnlineInfoItem::SetUserName(CString UserName)
{
	sUserName=UserName;
}
	
int  COnlineInfoItem::GetListenPort()
{
	return iListenPort;
}
int COnlineInfoItem::GetHeadID()
{
	return iHeadID;
}
CString COnlineInfoItem::GetIP()
{
	return sIP;
}
CString COnlineInfoItem::GetUserName()
{
	return sUserName;
}
COnlineInfoItem::COnlineInfoItem()
{
	next=NULL;
}
COnlineInfoItem::COnlineInfoItem(int Port,int HeadId,CString IP,CString UserName)
{
	iListenPort=Port;
	iHeadID=HeadId;
	sIP=IP;
	sUserName=UserName;
	next=NULL;
}
COnlineInfoItem::~COnlineInfoItem()
{
}
