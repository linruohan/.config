// TelOpt.cpp : implementation file
//

#include "stdafx.h"
#include "SerFrame.h"
#include "TelOptDlg.h"

#include "ShowAllChanTypeDlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif



/////////////////////////////////////////////////////////////////////////////
// CTelOptDlg dialog


CTelOptDlg::CTelOptDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CTelOptDlg::IDD, pParent)
{
	//{{AFX_DATA_INIT(CTelOptDlg)
	m_iInLineNum = 0;
	m_iInLine1 = 0;
	m_iInLine2 = 0;
	m_iInLine3 = 0;
	m_iInLine4 = 0;
	m_iInLine5 = 0;
	m_iInLine6 = 0;
	m_iOutLineNo = 0;
	//}}AFX_DATA_INIT
}


void CTelOptDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CTelOptDlg)
	DDX_Text(pDX, IDE_INLINENUM, m_iInLineNum);
	DDX_Text(pDX, IDE_INLINE1, m_iInLine1);
	DDX_Text(pDX, IDE_INLINE2, m_iInLine2);
	DDX_Text(pDX, IDE_INLINE3, m_iInLine3);
	DDX_Text(pDX, IDE_INLINE4, m_iInLine4);
	DDX_Text(pDX, IDE_INLINE5, m_iInLine5);
	DDX_Text(pDX, IDE_INLINE6, m_iInLine6);
	DDX_Text(pDX, IDE_OUTLINENO, m_iOutLineNo);
	//}}AFX_DATA_MAP
}


BEGIN_MESSAGE_MAP(CTelOptDlg, CDialog)
	//{{AFX_MSG_MAP(CTelOptDlg)
	ON_BN_CLICKED(IDB_CANCEL, On_Cancel)
	ON_BN_CLICKED(IDB_OK, On_Ok)
	ON_BN_CLICKED(IDC_SHOW_ALL_CHAN, OnShowAllChannel)
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CTelOptDlg message handlers

BOOL CTelOptDlg::PreTranslateMessage(MSG* pMsg) 
{
	if ( WM_KEYDOWN == pMsg->message ) {
		int nKey = (int) pMsg->wParam;
		if ( (nKey == VK_RETURN) || (nKey == VK_ESCAPE) )	//Ã»ÓÐVK_ENTER 
		return true;
	}
	return CDialog::PreTranslateMessage(pMsg);
}

void CTelOptDlg::On_Cancel() 
{
	EndDialog(0);
}

void CTelOptDlg::On_Ok() 
{
	UpdateData(true);
	
	CIniFile iniFile;

	iniFile.Create( "config.ini" );
	iniFile.SetVarInt ( "Telephone", "OutLineNO", m_iOutLineNo );
	iniFile.SetVarInt ( "Telephone", "InLineNum", m_iInLineNum );
	iniFile.SetVarInt ( "Telephone", "InLine1", m_iInLine1 );
	iniFile.SetVarInt ( "Telephone", "InLine2", m_iInLine2 );
	iniFile.SetVarInt ( "Telephone", "InLine3", m_iInLine3 );
	iniFile.SetVarInt ( "Telephone", "InLine4", m_iInLine4 );
	iniFile.SetVarInt ( "Telephone", "InLine5", m_iInLine5 );
	iniFile.SetVarInt ( "Telephone", "InLine6", m_iInLine6 );
	
	EndDialog(0);	
}

BOOL CTelOptDlg::OnInitDialog() 
{
	CDialog::OnInitDialog();
	
	CString sTemp;

	CIniFile iniFile;

	iniFile.Create( "config.ini" );
	iniFile.GetVarInt ( "Telephone", "OutLineNO", m_iOutLineNo );
	sTemp.Format( "%d", m_iOutLineNo );
	GetDlgItem(IDE_OUTLINENO)->SetWindowText(sTemp);

	iniFile.GetVarInt ( "Telephone", "InLineNum", m_iInLineNum );
	sTemp.Format( "%d", m_iInLineNum );
	GetDlgItem(IDE_INLINENUM)->SetWindowText(sTemp);

	iniFile.GetVarInt ( "Telephone", "InLine1", m_iInLine1 );
	sTemp.Format( "%d", m_iInLine1 );
	GetDlgItem(IDE_INLINE1)->SetWindowText(sTemp);
	
	iniFile.GetVarInt ( "Telephone", "InLine2", m_iInLine2 );
	sTemp.Format( "%d", m_iInLine2 );
	GetDlgItem(IDE_INLINE2)->SetWindowText(sTemp);
	
	iniFile.GetVarInt ( "Telephone", "InLine3", m_iInLine3 );
	sTemp.Format( "%d", m_iInLine3 );
	GetDlgItem(IDE_INLINE3)->SetWindowText(sTemp);

	iniFile.GetVarInt ( "Telephone", "InLine4", m_iInLine4 );
	sTemp.Format( "%d", m_iInLine4 );
	GetDlgItem(IDE_INLINE4)->SetWindowText(sTemp);

	iniFile.GetVarInt ( "Telephone", "InLine5", m_iInLine5 );
	sTemp.Format( "%d", m_iInLine5 );
	GetDlgItem(IDE_INLINE5)->SetWindowText(sTemp);

	iniFile.GetVarInt ( "Telephone", "InLine6", m_iInLine6 );
	sTemp.Format( "%d", m_iInLine6 );
	GetDlgItem(IDE_INLINE6)->SetWindowText(sTemp);
	
	return TRUE;  // return TRUE unless you set the focus to a control
	              // EXCEPTION: OCX Property Pages should return FALSE
}



void CTelOptDlg::OnShowAllChannel() 
{
	CShowAllChanTypeDlg  dlg;
	dlg.DoModal();
	
}
