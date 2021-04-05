//////////////////////////////////////////////////////////////////////////////////////////////////
//
// 文件: SerFrame.cpp	???????????????????
//
// 日期：2005年1月21日
//
// 作者: 吕宝虹 (C) All Rights Reserved
//
// 描述: 建立数据源
//
//////////////////////////////////////////////////////////////////////////////////////////////////
#include "stdafx.h"
#include "SerFrame.h"
#include "SerFrameDlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CSerFrameApp

BEGIN_MESSAGE_MAP(CSerFrameApp, CWinApp)
	//{{AFX_MSG_MAP(CSerFrameApp)
		// NOTE - the ClassWizard will add and remove mapping macros here.
		//    DO NOT EDIT what you see in these blocks of generated code!
	//}}AFX_MSG
	ON_COMMAND(ID_HELP, CWinApp::OnHelp)
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CSerFrameApp construction

CSerFrameApp::CSerFrameApp()
{
	// TODO: add construction code here,
	// Place all significant initialization in InitInstance
}

/////////////////////////////////////////////////////////////////////////////
// The one and only CSerFrameApp object

CSerFrameApp theApp;

/////////新来的////////////////////
#include "DefTypes.h"
#include <winsock2.h>
#include "OnLIneInfoQueue.h"
#include <afxdb.h>	
//#include <afxdao.h>	
CDatabase database;
SOCKET ListenSock;
SOCKADDR_IN local;
bool quit=false;
char   RecvBuf[DEFAULT_BUFFER_LENGTH];
COnLIneInfoQueue  OnLIneInfoQueue;
//////////////新来的///////////////////////////

/////////////////////////////////////////////////////////////////////////////
// CSerFrameApp initialization

BOOL CSerFrameApp::InitInstance()
{
	
	AfxInitRichEdit();
	
	
	// Initialize OLE libraries
	if (!AfxOleInit())
	{
		AfxMessageBox(IDP_OLE_INIT_FAILED);
		return FALSE;
	}


		
	AfxEnableControlContainer();

	// Standard initialization
	// If you are not using these features and wish to reduce the size
	//  of your final executable, you should remove from the following
	//  the specific initialization routines you do not need.

#ifdef _AFXDLL
	Enable3dControls();			// Call this when using MFC in a shared DLL
#else
	Enable3dControlsStatic();	// Call this when linking to MFC statically
#endif

	// Parse the command line to see if launched as OLE server
	if (RunEmbedded() || RunAutomated())
	{
		// Register all OLE server (factories) as running.  This enables the
		//  OLE libraries to create objects from other applications.
		COleTemplateServer::RegisterAll();
	}
	else
	{
		// When a server application is launched stand-alone, it is a good idea
		//  to update the system registry in case it has been damaged.
		COleObjectFactory::UpdateRegistryAll();
	}


	//----------设置数据源------------------
	SQLConfigDataSource(NULL,ODBC_ADD_DSN,
	"Microsoft Access Driver (*.mdb)\0",
		"DSN=NameList\0DBQ=data\\NameList.mdb\0DEFAULTDIR=data\0\0");
	//------end----设置数据源------------------


	CSerFrameDlg dlg;
	m_pMainWnd = &dlg;
	int nResponse = dlg.DoModal();
	if (nResponse == IDOK)
	{
		// TODO: Place code here to handle when the dialog is
		//  dismissed with OK
	}
	else if (nResponse == IDCANCEL)
	{
		// TODO: Place code here to handle when the dialog is
		//  dismissed with Cancel
	}

	// Since the dialog has been closed, return FALSE so that we exit the
	//  application, rather than start the application's message pump.
	return FALSE;
}

int CSerFrameApp::ExitInstance() 
{
	// TODO: Add your specialized code here and/or call the base class
	////////////新来的////////////////
	database.Close();//关闭数据源
	TRACE("\n数据库关闭\n");
	quit=true;
	closesocket(ListenSock);
	WSACleanup();
	//////////新来的////////////////////////
	return CWinApp::ExitInstance();
}
