// FaxOptDlg.cpp : implementation file
//

#include "stdafx.h"
#include "SerFrame.h"
#include "FaxOptDlg.h"
#include "CIniFile.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CFaxOptDlg dialog


CFaxOptDlg::CFaxOptDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CFaxOptDlg::IDD, pParent)
{
	//{{AFX_DATA_INIT(CFaxOptDlg)
	m_iOutLineNoWithFax = 0;
	//}}AFX_DATA_INIT
}


void CFaxOptDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CFaxOptDlg)
	DDX_Text(pDX, IDE_OUTLINEWITHFAX, m_iOutLineNoWithFax);
	//}}AFX_DATA_MAP
}


BEGIN_MESSAGE_MAP(CFaxOptDlg, CDialog)
	//{{AFX_MSG_MAP(CFaxOptDlg)
	ON_BN_CLICKED(IDB_OK, On_Ok)
	ON_BN_CLICKED(IDB_CANCEL, On_Cancel)
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CFaxOptDlg message handlers

BOOL CFaxOptDlg::OnInitDialog() 
{
	CDialog::OnInitDialog();
	
	CString sTemp;

	CIniFile iniFile;

	iniFile.Create( "config.ini" );
	iniFile.GetVarInt ( "Fax", "OutLineNOWithFax", m_iOutLineNoWithFax );
	sTemp.Format( "%d", m_iOutLineNoWithFax );
	GetDlgItem ( IDE_OUTLINEWITHFAX )->SetWindowText(sTemp);

	return TRUE;  // return TRUE unless you set the focus to a control
	              // EXCEPTION: OCX Property Pages should return FALSE
}

void CFaxOptDlg::On_Ok() 
{
	UpdateData ( true );

	CIniFile iniFile;

	iniFile.Create( "config.ini" );
	iniFile.SetVarInt ( "Fax", "OutLineNOWithFax", m_iOutLineNoWithFax );

	EndDialog (0);
}

void CFaxOptDlg::On_Cancel() 
{
	EndDialog (0);
}

BOOL CFaxOptDlg::PreTranslateMessage(MSG* pMsg) 
{
	if ( WM_KEYDOWN == pMsg->message ) {
		int nKey = (int) pMsg->wParam;
		if ( (nKey == VK_RETURN) || (nKey == VK_ESCAPE) )	//Ã»ÓÐVK_ENTER 
		return true;
	}	
	return CDialog::PreTranslateMessage(pMsg);
}
