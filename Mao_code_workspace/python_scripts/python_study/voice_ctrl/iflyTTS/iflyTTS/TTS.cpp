// TTS.cpp : Defines the class behaviors for the application.
//

#include "stdafx.h"
#include "TTS.h"
#include "TTSDlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CTTSApp

BEGIN_MESSAGE_MAP(CTTSApp, CWinApp)
	ON_COMMAND(ID_HELP, &CWinApp::OnHelp)
END_MESSAGE_MAP()


// CTTSApp construction

CTTSApp::CTTSApp()
{
	// TODO: add construction code here,
	// Place all significant initialization in InitInstance
}


// The one and only CTTSApp object

CTTSApp theApp;


// CTTSApp initialization

BOOL CTTSApp::InitInstance()
{
	// InitCommonControlsEx() is required on Windows XP if an application
	// manifest specifies use of ComCtl32.dll version 6 or later to enable
	// visual styles.  Otherwise, any window creation will fail.
	INITCOMMONCONTROLSEX InitCtrls;
	InitCtrls.dwSize = sizeof(InitCtrls);
	// Set this to include all the common control classes you want to use
	// in your application.
	InitCtrls.dwICC = ICC_WIN95_CLASSES;
	InitCommonControlsEx(&InitCtrls);

	CWinApp::InitInstance();

	AfxEnableControlContainer();

	// Standard initialization
	// If you are not using these features and wish to reduce the size
	// of your final executable, you should remove from the following
	// the specific initialization routines you do not need
	// Change the registry key under which our settings are stored
	// TODO: You should modify this string to be something appropriate
	// such as the name of your company or organization
	SetRegistryKey(_T("Local AppWizard-Generated Applications"));

	CTTSDlg dlg;
	//HRESULT hr;
	//hr = dlg.InitSapi();
	//if(!SUCCEEDED(hr))
	//{
	//	::AfxMessageBox(_T("≥ı ºªØTTS ß∞‹£¨«Î÷ÿ ‘!"));
	//	exit(0);
	//}
	m_pMainWnd = &dlg;
	INT_PTR nResponse = dlg.DoModal();
	dlg.ReleaseSapi();


	// Since the dialog has been closed, return FALSE so that we exit the
	//  application, rather than start the application's message pump.
	return FALSE;
}
