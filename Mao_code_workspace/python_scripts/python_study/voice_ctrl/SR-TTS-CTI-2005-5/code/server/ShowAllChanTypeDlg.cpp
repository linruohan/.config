// ShowAllChanTypeDlg.cpp : implementation file
//

#include "stdafx.h"
#include "SerFrame.h"
#include "ShowAllChanTypeDlg.h"

#include "NewSig.h"
#include "Tc08a32.h"
#include "Conf95.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CShowAllChanTypeDlg dialog


CShowAllChanTypeDlg::CShowAllChanTypeDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CShowAllChanTypeDlg::IDD, pParent)
{
	//{{AFX_DATA_INIT(CShowAllChanTypeDlg)
		// NOTE: the ClassWizard will add member initialization here
	//}}AFX_DATA_INIT
}


void CShowAllChanTypeDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CShowAllChanTypeDlg)
	DDX_Control(pDX, IDL_ALLCHENNELTYPE, m_ChannelList);
	//}}AFX_DATA_MAP
}


BEGIN_MESSAGE_MAP(CShowAllChanTypeDlg, CDialog)
	//{{AFX_MSG_MAP(CShowAllChanTypeDlg)
	ON_WM_DESTROY()
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CShowAllChanTypeDlg message handlers

BOOL CShowAllChanTypeDlg::OnInitDialog() 
{
	CDialog::OnInitDialog();
	
	m_ChannelList.InsertColumn( 0,"通道号" );
	m_ChannelList.InsertColumn( 1,"通道类型" );
	m_ChannelList.InsertColumn( 2,"其他" );

	RECT rect;
	m_ChannelList.GetWindowRect(&rect);
	int wid = rect.right - rect.left;
	m_ChannelList.SetColumnWidth(0,wid/3);
	m_ChannelList.SetColumnWidth(1,wid/3);
	m_ChannelList.SetColumnWidth(2,wid/3);

	m_ChannelList.SetExtendedStyle(LVS_EX_FULLROWSELECT|LVS_EX_GRIDLINES|LVS_EX_HEADERDRAGDROP);

	m_ChannelList.DeleteAllItems();
	
	int DriverOpenFlag = ::LoadDRV ();	//加载电话卡驱动程序
	if ( DriverOpenFlag ) {
		::ShowError ( "打开设备驱动程序错误---LoadDRV()", "加载驱动程序失败" );
		return false;
	}

	int iChannelNum = ::CheckValidCh();
	if ( ::EnableCard ( iChannelNum, 1024*8 ) != (long) 0 ) {
		::FreeDRV ();
		::ShowError ( "初始化电话卡的硬件失败---EnableCard()", "设备初始化失败" );
		return false;
	}

	CString sTemp1, sTemp2;
	
	for ( int wChanNo = iChannelNum -1; wChanNo>=0 ; wChanNo-- ) {
		switch ( ::CheckChTypeNew ( wChanNo ) ) {
			case CHTYPE_TRUNK:
				sTemp1.LoadString( IDS_CHTYPE_TRUNK );
				break;

			case CHTYPE_USER:
				sTemp1.LoadString( IDS_CHTYPE_USER );
				break;

			case CHTYPE_EMPTY:
				sTemp1.LoadString( IDS_CHTYPE_EMPTY );
				break;

			case CHTYPE_RECORD:
				sTemp1.LoadString( IDS_CHTYPE_RECORD );
				break;

			default:
				sTemp1 = "未知类型";
				break;
		}

		sTemp2.Format ( "%d", wChanNo );
		m_ChannelList.InsertItem( 0, sTemp2 );
		m_ChannelList.SetItemText( 0, 1, sTemp1 );
		m_ChannelList.SetItemText( 0, 2, "" );
	}

	return TRUE;  // return TRUE unless you set the focus to a control
	              // EXCEPTION: OCX Property Pages should return FALSE
}

void CShowAllChanTypeDlg::OnDestroy() 
{
	CDialog::OnDestroy();
	
	::DisableCard ();	//关闭电话卡的硬件，释放缓冲区。程序结束(包括正常和不正常退出)时需调用此函数。
	::FreeDRV ();		//关闭驱动程序。	
}
