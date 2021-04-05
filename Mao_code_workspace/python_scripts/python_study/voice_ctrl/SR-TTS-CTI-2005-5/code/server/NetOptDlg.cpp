// NetOptDlg.cpp : implementation file
//

#include "stdafx.h"
#include "SerFrame.h"
#include "NetOptDlg.h"
#include "CIniFile.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CNetOptDlg dialog


CNetOptDlg::CNetOptDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CNetOptDlg::IDD, pParent)
{
	//{{AFX_DATA_INIT(CNetOptDlg)
	m_sServerIP = _T("");
	m_iPort = 0;
	//}}AFX_DATA_INIT
}


void CNetOptDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CNetOptDlg)
	DDX_Text(pDX, IDE_SERVER_IP, m_sServerIP);
	DDX_Text(pDX, IDE_SERVER_PORT, m_iPort);
	//}}AFX_DATA_MAP
}


BEGIN_MESSAGE_MAP(CNetOptDlg, CDialog)
	//{{AFX_MSG_MAP(CNetOptDlg)
	ON_BN_CLICKED(IDB_OK, On_Ok)
	ON_BN_CLICKED(IDB_CANCEL, On_Cancel)
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CNetOptDlg message handlers

BOOL CNetOptDlg::PreTranslateMessage(MSG* pMsg) 
{
	if ( WM_KEYDOWN == pMsg->message ) {
		int nKey = (int) pMsg->wParam;
		if ( (nKey == VK_RETURN) || (nKey == VK_ESCAPE) )	//Ã»ÓÐVK_ENTER 
		return true;
	}
	return CDialog::PreTranslateMessage(pMsg);
}

void CNetOptDlg::On_Ok() 
{
	UpdateData(true);
	
	CIniFile iniFile;

	iniFile.Create( "config.ini" );
	
	iniFile.SetVarStr ( "Network", "ServerIP", m_sServerIP );
	iniFile.SetVarInt ( "Network", "ServerPort", m_iPort );
	
	EndDialog(0);
}

void CNetOptDlg::On_Cancel() 
{
	EndDialog(0);		
}

BOOL CNetOptDlg::OnInitDialog() 
{
	CDialog::OnInitDialog();
	
	CIniFile iniFile;

	iniFile.Create( "config.ini" );
	
	iniFile.GetVarStr ( "Network", "ServerIP", m_sServerIP );
	GetDlgItem(IDE_SERVER_IP)->SetWindowText(m_sServerIP);

	CString sTemp;
	iniFile.GetVarInt ( "Network", "ServerPort", m_iPort );
	sTemp.Format( "%d", m_iPort );
	GetDlgItem(IDE_SERVER_PORT)->SetWindowText(sTemp);
	
	return TRUE;  // return TRUE unless you set the focus to a control
	              // EXCEPTION: OCX Property Pages should return FALSE
}
