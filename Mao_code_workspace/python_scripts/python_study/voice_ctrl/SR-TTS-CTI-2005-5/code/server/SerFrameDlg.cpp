//////////////////////////////////////////////////////////////////////////////////////////////////
//
// 文件: SerFrameDlg.cpp
//
// 日期：2005年1月21日
//
// 作者: 吕宝虹 (C) All Rights Reserved
//
// 描述: 程序的主界面
//
//////////////////////////////////////////////////////////////////////////////////////////////////

#include "stdafx.h"
#include "SerFrame.h"
#include "SerFrameDlg.h"
#include "DlgProxy.h"
#include "TelOptDlg.h"
#include "NetOptDlg.h"
#include "FaxOptDlg.h"
#include "CIniFile.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif
////////////////NET////////////////////
#include "process.h"
#include "DefTypes.h"
extern  DWORD WINAPI ProcessThread(LPVOID lpParam);
//*绑定数据源
#include "odbcinst.h"//////////////////
#pragma  comment (lib,"Odbccp32")
/////////////////////////////////////////////////////////////////////////////

extern	CDatabase database;
extern	SOCKET ListenSock;
extern	SOCKADDR_IN local;
extern	COnLIneInfoQueue  OnLIneInfoQueue;
///////////			声明外部变量		/////////////////
///////////////////NET/////////////////////

class CAboutDlg : public CDialog
{
public:
	CAboutDlg();

// Dialog Data
	//{{AFX_DATA(CAboutDlg)
	enum { IDD = IDD_ABOUTBOX };
	//}}AFX_DATA

	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CAboutDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:
	//{{AFX_MSG(CAboutDlg)
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialog(CAboutDlg::IDD)
{
	//{{AFX_DATA_INIT(CAboutDlg)
	//}}AFX_DATA_INIT
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CAboutDlg)
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialog)
	//{{AFX_MSG_MAP(CAboutDlg)
		// No message handlers
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CSerFrameDlg dialog

IMPLEMENT_DYNAMIC(CSerFrameDlg, CDialog);

CSerFrameDlg::CSerFrameDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CSerFrameDlg::IDD, pParent)
{
	//{{AFX_DATA_INIT(CSerFrameDlg)
	m_szFaxDialNo = _T("");
	//}}AFX_DATA_INIT
	// Note that LoadIcon does not require a subsequent DestroyIcon in Win32
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
	m_pAutoProxy = NULL;
	m_bTelRun = false;
}

CSerFrameDlg::~CSerFrameDlg()
{
	// If there is an automation proxy for this dialog, set
	//  its back pointer to this dialog to NULL, so it knows
	//  the dialog has been deleted.
	if (m_pAutoProxy != NULL)
		m_pAutoProxy->m_pDialog = NULL;
}

void CSerFrameDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CSerFrameDlg)
	DDX_Control(pDX, IDL_FAXREPORT, m_FaxReport);
	DDX_Control(pDX, ID_REPORT, m_TelReport);
	DDX_Text(pDX, IDE_FAX_DIAL_NO, m_szFaxDialNo);
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CSerFrameDlg, CDialog)
	//{{AFX_MSG_MAP(CSerFrameDlg)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDB_MANAGENAME, OnManageName)
	ON_BN_CLICKED(IDB_CLOSE, OnClose)
	ON_BN_CLICKED(IDB_FAXOPT, OnFaxopt)
	ON_BN_CLICKED(IDB_START, OnStart)
	ON_BN_CLICKED(IDB_STOP, OnStop)
	ON_WM_TIMER()
	ON_WM_DESTROY()
	ON_BN_CLICKED(IDB_TELOPT, OnTelOpt)
	ON_BN_CLICKED(IDB_NETOPT, OnNetOpt)
	ON_BN_CLICKED(IDB_SENDFAX_SERFRAME, OnSendFax)
	ON_BN_CLICKED(IDC_BUTTON1, OnTest)
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CSerFrameDlg message handlers

BOOL CSerFrameDlg::OnInitDialog()
{
	CDialog::OnInitDialog();
	
	// Add "About..." menu item to system menu.

	// IDM_ABOUTBOX must be in the system command range.
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if ( pSysMenu != NULL ) {
		CString strAboutMenu;
		strAboutMenu.LoadString(IDS_ABOUTBOX);
		if ( !strAboutMenu.IsEmpty() ) {
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// Set the icon for this dialog.  The framework does this automatically
	//  when the application's main window is not a dialog
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon
	
	//----初始化列表的字段---------------------------------------------------
	m_TelReport.InsertColumn( 0, "通道号" );
	m_TelReport.InsertColumn( 1, "通道类型" );
	m_TelReport.InsertColumn( 2, "通道状态" );
	m_TelReport.InsertColumn( 3, "主叫号码" );
	m_TelReport.InsertColumn( 4, "录音文件" );
	//m_TelReport.InsertColumn( 4, "按键" );
	//m_TelReport.InsertColumn( 5, "录音文件" );
	//m_TelReport.InsertColumn( 6, "留位" );

	RECT rect;
	m_TelReport.GetWindowRect(&rect);
	int wid = rect.right - rect.left;
	m_TelReport.SetColumnWidth(0,wid/8);
	m_TelReport.SetColumnWidth(1,wid/6);
	m_TelReport.SetColumnWidth(2,wid/6);
	m_TelReport.SetColumnWidth(3,wid/6);
	m_TelReport.SetColumnWidth(4,wid/8*3);
	//m_TelReport.SetColumnWidth(5,wid/7);
	//m_TelReport.SetColumnWidth(6,wid/7);

	m_TelReport.SetExtendedStyle(LVS_EX_FULLROWSELECT|LVS_EX_GRIDLINES|LVS_EX_HEADERDRAGDROP);
	//------END--初始化列表的字段------------------------------------
	m_FaxReport.InsertColumn( 0, "通道号" );
	m_FaxReport.InsertColumn( 1, "通道状态" );
	m_FaxReport.InsertColumn( 2, "主叫号码" );
	m_FaxReport.InsertColumn( 3, "正在接受的文件" );
	
	m_FaxReport.GetWindowRect(&rect);
	wid = rect.right - rect.left;
	m_FaxReport.SetColumnWidth(0,wid/4);
	m_FaxReport.SetColumnWidth(1,wid/4);
	m_FaxReport.SetColumnWidth(2,wid/4);
	m_FaxReport.SetColumnWidth(3,wid/4);

	m_FaxReport.SetExtendedStyle(LVS_EX_FULLROWSELECT|LVS_EX_GRIDLINES|LVS_EX_HEADERDRAGDROP);

	NetInit();

	return TRUE;  // return TRUE  unless you set the focus to a control
}

void CSerFrameDlg::OnSysCommand ( UINT nID, LPARAM lParam )
{
	if ( (nID & 0xFFF0) == IDM_ABOUTBOX ) {
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else {
		CDialog::OnSysCommand(nID, lParam);
	}
}

// If you add a minimize button to your dialog, you will need the code below
//  to draw the icon.  For MFC applications using the document/view model,
//  this is automatically done for you by the framework.

void CSerFrameDlg::OnPaint() 
{
	if ( IsIconic() ) {
		CPaintDC dc(this); // device context for painting

		SendMessage(WM_ICONERASEBKGND, (WPARAM) dc.GetSafeHdc(), 0);

		// Center icon in client rectangle
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// Draw the icon
		dc.DrawIcon(x, y, m_hIcon);
	}
	else {
		CDialog::OnPaint();
	}
}

// The system calls this to obtain the cursor to display while the user drags
//  the minimized window.
HCURSOR CSerFrameDlg::OnQueryDragIcon()
{
	return (HCURSOR) m_hIcon;
}

// Automation servers should not exit when a user closes the UI
//  if a controller still holds on to one of its objects.  These
//  message handlers make sure that if the proxy is still in use,
//  then the UI is hidden but the dialog remains around if it
//  is dismissed.

BOOL CSerFrameDlg::CanExit()
{
	// If the proxy object is still around, then the automation
	//  controller is still holding on to this application.  Leave
	//  the dialog around, but hide its UI.
	if ( m_pAutoProxy != NULL ) {
		ShowWindow  ( SW_HIDE );
		return FALSE;
	}
	return TRUE;
}

//屏蔽对ESC键和ENTER键的自动响应
BOOL CSerFrameDlg::PreTranslateMessage(MSG* pMsg) 
{
	if ( WM_KEYDOWN == pMsg->message ) {
		int nKey = (int) pMsg->wParam;
		if ( (nKey == VK_RETURN) || (nKey == VK_ESCAPE) )	//没有VK_ENTER 
		return true;
	}
	return CDialog::PreTranslateMessage(pMsg);
}

void CSerFrameDlg::OnManageName() 
{
	//停止服务
	CNameList namelist;		//打开姓名管理界面
	namelist.DoModal ();
	//开始服务
}

void CSerFrameDlg::OnClose() 
{
	this->EndDialog(0);	
}

/////////////////////test
void CSerFrameDlg::OnFaxopt() 
{
	CFaxOptDlg faxopt;
	faxopt.DoModal ();
}

//启动服务
void CSerFrameDlg::OnStart() 
{
	if ( !m_bTelRun ) {
		if ( !m_Tel.InitSystem () ) {
			return;
		}
		m_bTelRun = true;
		m_nTimer = SetTimer ( 1, 100, NULL );	//设置一个计时器
	}

	//改变按钮状态
	CButton *button;
	button = (CButton *)GetDlgItem ( IDB_START );
	button->EnableWindow( false );
	button = (CButton *)GetDlgItem ( IDB_TELOPT );
	button->EnableWindow( false );
	//button = (CButton *)GetDlgItem ( IDB_MANAGENAME );
	//button->EnableWindow( false );
	button = (CButton *)GetDlgItem ( IDB_STOP );
	button->EnableWindow( true );
	button = (CButton *)GetDlgItem ( IDB_SENDFAX_SERFRAME );
	button->EnableWindow( true );
}

//停止服务
void CSerFrameDlg::OnStop() 
{
	if ( m_bTelRun ) {
		KillTimer( 1 );	//必须先停止计时器，再退出电话系统。
		m_TelReport.DeleteAllItems();
		m_Tel.ExitSystem ();
		m_bTelRun = false;
	}
	
	//改变按钮状态
	CButton *button;
	button = (CButton *)GetDlgItem ( IDB_STOP );
	button->EnableWindow( false );
	button = (CButton *)GetDlgItem ( IDB_START );
	button->EnableWindow( true );
	button = (CButton *)GetDlgItem ( IDB_TELOPT );
	button->EnableWindow( true );
	//button = (CButton *)GetDlgItem ( IDB_MANAGENAME );
	//button->EnableWindow( true );
	button = (CButton *)GetDlgItem ( IDB_SENDFAX_SERFRAME );
	button->EnableWindow( false );
	
}

//处理电话处理的循环，定时处理电话事件
void CSerFrameDlg::OnTimer(UINT nIDEvent) 
{
	if ( (nIDEvent == 1) && m_bTelRun ) {
		//处理电话，显示电话状态
		m_Tel.TelProc();
		ShowTelState();
		
		//处理传真，显示传真状态
		m_Tel.FaxProc();
		ShowFaxState();
	}
	CDialog::OnTimer(nIDEvent);
}

//先是电话卡线路的状态
void CSerFrameDlg::ShowTelState()
{
	static ChannelStruct   line ;	//线路状态的数组
	char temp[64];
	CString strTemp;

	m_TelReport.DeleteAllItems();

	int num = m_Tel.GetChannelsNum();
	
	for ( int i=num-1; i>=0; i-- ) {
		m_Tel.GetLineState( &line, i );
		
		sprintf( temp, "%d", line.wChannelNo );	//通道号
		m_TelReport.InsertItem( 0, temp );
				
		switch ( line.iType ) {
			case CHTYPE_USER:
				strTemp.LoadString ( IDS_CHTYPE_USER );
				break;
			
			case CHTYPE_TRUNK:
				strTemp.LoadString ( IDS_CHTYPE_TRUNK );
				break;

			case CHTYPE_EMPTY:
				strTemp.LoadString ( IDS_CHTYPE_EMPTY );
				break;
			
			case CHTYPE_RECORD:
				strTemp.LoadString ( IDS_CHTYPE_RECORD );
				break;
		}
		
		m_TelReport.SetItemText( 0, 1, strTemp );
		
		switch ( line.iState ) {
			case CH_FREE:
				strTemp.LoadString ( IDS_CH_FREE );
				break;
			case CH_OFFHOOK:
				strTemp.LoadString ( IDS_CH_OFFHOOK );
				break;
			case CH_WELCOME:
				strTemp.LoadString ( IDS_CH_WELCOME );
				break;
			case CH_SELECT:
				strTemp.LoadString ( IDS_CH_SELECT );
				break;
			case CH_RECORD_MESSAGE_START:
				strTemp.LoadString ( IDS_CH_RECORD_MESSAGE_START );
				break;
			case CH_RECORD_MESSAGE_ING:
				strTemp.LoadString ( IDS_CH_RECORD_MESSAGE_ING );
				break;
			case CH_RECORD_MESSAGE_END:
				strTemp.LoadString ( IDS_CH_RECORD_MESSAGE_END );
				break;
			case CH_CALL_BY_SPEECH_START:
				strTemp.LoadString ( IDS_CH_CALL_BY_SPEECH_START );
				break;
			case CH_CALL_BY_SPEECH_RECORDING:
				strTemp.LoadString ( IDS_CH_CALL_BY_SPEECH_RECORDING );
				break;
			case CH_CALL_BY_SPEECH_RECONITION:
				strTemp.LoadString ( IDS_CH_CALL_BY_SPEECH_RECONITION );
				break;
			case CH_CALL_BY_DTMF_START:
				strTemp.LoadString ( IDS_CH_CALL_BY_DTMF_START );
				break;
			case CH_CALL_BY_DTMF_GETDTMF:
				strTemp.LoadString ( IDS_CH_CALL_BY_DTMF_GETDTMF );
				break;
			case CH_CALL_BY_DTMF_SEARCHING:
				strTemp.LoadString ( IDS_CH_CALL_BY_DTMF_SEARCHING );
				break;
			case CH_INLINE_BUSY:
				strTemp.LoadString ( IDS_CH_INLINE_BUSY );
				break;
			case CH_INLINE_HANGUP:
				strTemp.LoadString ( IDS_CH_INLINE_HANGUP );
				break;
			case CH_TALKING_WITH_IN:
				strTemp.LoadString ( IDS_CH_TALKING_WITH_IN );
				break;
			case CH_CHOICE_MESSAGE:
				strTemp.LoadString ( IDS_CH_CHOICE_MESSAGE );
				break;
			case CH_PLAY_MESSAGE_START:
				strTemp.LoadString ( IDS_CH_PLAY_MESSAGE_START );
				break;
			case CH_PLAY_MESSAGE_ING:
				strTemp.LoadString ( IDS_CH_PLAY_MESSAGE_ING );
				break;
			case CH_PLAY_MESSAGE_END:
				strTemp.LoadString ( IDS_CH_PLAY_MESSAGE_END );
				break;
			case CH_RINGING:
				strTemp.LoadString ( IDS_CH_RINGING );
				break;
			case CH_WAIT_OFFHOOK:
				strTemp.LoadString ( IDS_CH_WAIT_OFFHOOK );
				break;
			case CH_NO_LISTEN:
				strTemp.LoadString ( IDS_CH_NO_LISTEN );
				break;
			case CH_FEED_OFFHOOK:
				strTemp.LoadString ( IDS_CH_FEED_OFFHOOK );
				break;
			case CH_WAIT_LINK:
				strTemp.LoadString ( IDS_CH_WAIT_LINK );
				break;
			case CH_TALKING_WITH_OUT:
				strTemp.LoadString ( IDS_CH_TALKING_WITH_OUT );
				break;
			case CH_OUT_HANGUP:
				strTemp.LoadString ( IDS_CH_OUT_HANGUP );
				break;
			case CH_WAIT_IN_HANGUP:
				strTemp.LoadString ( IDS_CH_WAIT_IN_HANGUP );
				break;
			case CH_EMPTY:
				strTemp.LoadString ( IDS_CH_EMPTY );
				break;
		}
		
		m_TelReport.SetItemText( 0, 2, strTemp );
		
		m_TelReport.SetItemText( 0, 3, line.sCallerID );//来电号码

		m_TelReport.SetItemText( 0, 4, line.sNowRecordFileName );//录音文件
	}
}

//如果电话卡系统还在运行的话则关闭电话
void CSerFrameDlg::OnDestroy() 
{
	CDialog::OnDestroy();
	
	if ( m_bTelRun ) {
		m_Tel.ExitSystem();
		m_bTelRun = false;
	}
}

void CSerFrameDlg::OnTelOpt() 
{
	CTelOptDlg teldlg;
	teldlg.DoModal();
}

void CSerFrameDlg::OnNetOpt() 
{
	CNetOptDlg	NetOptDlg;
	NetOptDlg.DoModal();
}

void CSerFrameDlg::ShowFaxState()
{
	
	if ( m_Tel.IsUseFax() ) {
	
		static		FaxChnlStruct	faxstruct;
		char		temp[64];
		CString		strTemp;

		m_FaxReport.DeleteAllItems();

		m_Tel.GetFaxChnlState( & faxstruct );
			
		sprintf( temp, "%d", faxstruct.wChannelNo );	//通道号
		m_FaxReport.InsertItem( 0, temp );
			
		switch ( faxstruct.iState ) {
			case CH_FREE:
				strTemp.LoadString ( IDS_CH_FREE );
				break;
			case CH_OFFHOOK:
				strTemp.LoadString ( IDS_CH_OFFHOOK );
				break;
			case CH_WELCOME:
				strTemp.LoadString ( IDS_CH_WELCOME );
				break;
			case CH_SELECT:
				strTemp.LoadString ( IDS_CH_SELECT );
				break;
			case CH_RECORD_MESSAGE_START:
				strTemp.LoadString ( IDS_CH_RECORD_MESSAGE_START );
				break;
			case CH_RECORD_MESSAGE_ING:
				strTemp.LoadString ( IDS_CH_RECORD_MESSAGE_ING );
				break;
			case CH_RECORD_MESSAGE_END:
				strTemp.LoadString ( IDS_CH_RECORD_MESSAGE_END );
				break;
			case CH_CALL_BY_SPEECH_START:
				strTemp.LoadString ( IDS_CH_CALL_BY_SPEECH_START );
				break;
			case CH_CALL_BY_SPEECH_RECORDING:
				strTemp.LoadString ( IDS_CH_CALL_BY_SPEECH_RECORDING );
				break;
			case CH_CALL_BY_SPEECH_RECONITION:
				strTemp.LoadString ( IDS_CH_CALL_BY_SPEECH_RECONITION );
				break;
			case CH_CALL_BY_DTMF_START:
				strTemp.LoadString ( IDS_CH_CALL_BY_DTMF_START );
				break;
			case CH_CALL_BY_DTMF_GETDTMF:
				strTemp.LoadString ( IDS_CH_CALL_BY_DTMF_GETDTMF );
				break;
			case CH_CALL_BY_DTMF_SEARCHING:
				strTemp.LoadString ( IDS_CH_CALL_BY_DTMF_SEARCHING );
				break;
			case CH_INLINE_BUSY:
				strTemp.LoadString ( IDS_CH_INLINE_BUSY );
				break;
			case CH_INLINE_HANGUP:
				strTemp.LoadString ( IDS_CH_INLINE_HANGUP );
				break;
			case CH_TALKING_WITH_IN:
				strTemp.LoadString ( IDS_CH_TALKING_WITH_IN );
				break;
			case CH_CHOICE_MESSAGE:
				strTemp.LoadString ( IDS_CH_CHOICE_MESSAGE );
				break;
			case CH_PLAY_MESSAGE_START:
				strTemp.LoadString ( IDS_CH_PLAY_MESSAGE_START );
				break;
			case CH_PLAY_MESSAGE_ING:
				strTemp.LoadString ( IDS_CH_PLAY_MESSAGE_ING );
				break;
			case CH_PLAY_MESSAGE_END:
				strTemp.LoadString ( IDS_CH_PLAY_MESSAGE_END );
				break;
			case CH_RINGING:
				strTemp.LoadString ( IDS_CH_RINGING );
				break;
			case CH_WAIT_OFFHOOK:
				strTemp.LoadString ( IDS_CH_WAIT_OFFHOOK );
				break;
			case CH_NO_LISTEN:
				strTemp.LoadString ( IDS_CH_NO_LISTEN );
				break;
			case CH_FEED_OFFHOOK:
				strTemp.LoadString ( IDS_CH_FEED_OFFHOOK );
				break;
			case CH_WAIT_LINK:
				strTemp.LoadString ( IDS_CH_WAIT_LINK );
				break;
			case CH_TALKING_WITH_OUT:
				strTemp.LoadString ( IDS_CH_TALKING_WITH_OUT );
				break;
			case CH_OUT_HANGUP:
				strTemp.LoadString ( IDS_CH_OUT_HANGUP );
				break;
			case CH_WAIT_IN_HANGUP:
				strTemp.LoadString ( IDS_CH_WAIT_IN_HANGUP );
				break;
			case CH_EMPTY:
				strTemp.LoadString ( IDS_CH_EMPTY );
				break;
			case CH_RECEIVE_FAX_LINK:
				strTemp.LoadString ( IDS_CH_RECEIVE_FAX_LINK );
				break;
			
			case CH_RECEIVE_FAX_START:
				strTemp.LoadString ( IDS_CH_RECEIVE_FAX_START );
				break;
			
			case CH_RECEIVE_FAX_ING:
				strTemp.LoadString ( IDS_CH_RECEIVE_FAX_ING );
				break;
			case CH_RECEIVE_FAX_END:
				strTemp.LoadString ( IDS_CH_RECEIVE_FAX_END );
				break;
			
			
			case CH_SEND_FAX_LINK:
				strTemp.LoadString ( IDS_CH_SEND_FAX_LINK );
				break;
			case CH_SEND_FAX_DAIL:
				strTemp.LoadString ( IDS_CH_SEND_FAX_DAIL );
				break;
			case CH_SEND_FAX_START:
				strTemp.LoadString ( IDS_CH_SEND_FAX_START );
				break;
			case CH_SEND_FAX_ING:
				strTemp.LoadString ( IDS_CH_SEND_FAX_ING );
				break;
			case CH_SEND_FAX_END:
				strTemp.LoadString ( IDS_CH_SEND_FAX_END );
				break;

		}
			
		m_FaxReport.SetItemText( 0, 1, strTemp );
		
		m_FaxReport.SetItemText( 0, 2, faxstruct.sCallerID );//来电号码

		m_FaxReport.SetItemText( 0, 2, faxstruct.sNowRecFaxName );//接受的传真文件
	}
}

//弹出发送传真的对话框
void CSerFrameDlg::OnSendFax() 
{
	CString szPathName;
	char sSendFileName[128];
	char sFaxDialNo[28];
	UpdateData(true);
	
	if (  !m_Tel.IsUseFax() ) {
		AfxMessageBox ( "没有启动传真服务" );
		return;
	}
	
	if ( m_szFaxDialNo.GetLength() == 0 ) {
		AfxMessageBox( "请填写你要发传真的目标号码" );
		return;
	}
	else {
		strcpy ( sFaxDialNo, m_szFaxDialNo.GetBuffer(0) );
	}

	CFileDialog dlg ( true, "bfx", "*.bfx" );
	if ( dlg.DoModal() == IDOK ) {
		szPathName = dlg.GetPathName();
		strcpy ( sSendFileName, szPathName.GetBuffer(0) );
		m_Tel.SendFax ( sFaxDialNo, sSendFileName );
	}
}

void CSerFrameDlg::NetInit()
{
	SQLConfigDataSource(NULL,ODBC_ADD_DSN,
		"Microsoft Access Driver (*.mdb)\0",
		"DSN=CHAT\0DBQ=data\\chat.mdb\0DEFAULTDIR=data\0\0");
	
	//连接数据源,打开数据库.
	BOOL bStatus=FALSE;//数据库是否已经成功打开
	database.SetLoginTimeout(3);
	
	bStatus=database.OpenEx(_T("DSN=CHAT"));
	if(bStatus)
		TRACE("\n数据库已经打开\n");
	else
		TRACE("\n数据库打开失败\n");
	
	CIniFile	ini;
	ini.Create( "config.ini" );
	CString		ServerIP;
	int				ServerPort;
	ini.GetVarInt("Network","ServerPort",ServerPort);
	ini.GetVarStr("Network","ServerI",ServerIP);

	WSADATA        wsd;
	if (WSAStartup(MAKEWORD(2,2), &wsd) != 0)
    {
        TRACE("WSAStartup failed!\n");
    }
	ListenSock= socket(AF_INET, SOCK_DGRAM, 0);
	local.sin_family = AF_INET;
    local.sin_port = htons((short)ServerPort);
    local.sin_addr.s_addr = inet_addr((LPSTR)(LPCTSTR)ServerIP);
	if (bind(ListenSock, (SOCKADDR *)&local, sizeof(local)) == SOCKET_ERROR)
    {
		TRACE("bind() failed : %d\n", WSAGetLastError());
		MessageBox("bind()出错");
		return ;
	}
	

	HANDLE         hThread;
	DWORD         dwThreadId;
	hThread = ::CreateThread(NULL, 0, ProcessThread, 
		(LPVOID)ListenSock, 0, &dwThreadId);
	CloseHandle(hThread);	
}

void CSerFrameDlg::OnTest() 
{
	CLaneTel::SendMsg("1");
	
}
