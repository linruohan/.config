// LoginMessage.h: interface for the CLoginMessage class.
//
//////////////////////////////////////////////////////////////////////

#if !defined(AFX_LOGINMESSAGE_H__3A870B3F_C9BB_47B9_B556_E154227B520B__INCLUDED_)
#define AFX_LOGINMESSAGE_H__3A870B3F_C9BB_47B9_B556_E154227B520B__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

class CLoginMessage  
{
    public:
         
         CLoginMessage(char *RecvBuf);
         
         char* GetLoginName();
         char* GetLoginPassword();
         int   GetLoginHeadID();
         int   GetClientPort();
    private:
         
         char  LoginMessage[120];
         char  LoginName[50];
         char  LoginPassword[50];
         
         int   GetLoginNameLen();
         int   GetLoginPasswordLen();      

};

#endif // !defined(AFX_LOGINMESSAGE_H__3A870B3F_C9BB_47B9_B556_E154227B520B__INCLUDED_)
