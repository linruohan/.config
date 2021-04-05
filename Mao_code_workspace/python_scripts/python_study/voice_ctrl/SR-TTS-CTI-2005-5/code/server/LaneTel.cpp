#include "stdafx.h"
#include "LaneTel.h"
#include "CIniFile.h"

#include "CLog.h"

/////////////////////////////////////
#include "OnLIneInfoQueue.h"
#include <winsock2.h>
extern	SOCKET ListenSock;
extern	SOCKADDR_IN local;
extern	COnLIneInfoQueue  OnLIneInfoQueue;
///////////////////////////////////
#ifdef _DEBUG
#undef THIS_FILE
static char THIS_FILE[]=__FILE__;
#define new DEBUG_NEW
#endif

CLaneTel::CLaneTel()
{
	m_bUseFax		= false;
	m_pFaxChannel	= NULL;
}

//------------------内部调用--辅助函数--------------------
//得到声音的路径
void CLaneTel::GetVoicePath()
{
	GetCurrentDirectory ( 100, m_sVoicePath );
	strcat ( m_sVoicePath, "\\sound\\" );
}
//得到要录音的路径
void CLaneTel::GetRecordPath()
{
	GetCurrentDirectory ( 100, m_sRecordPath );
	strcat ( m_sRecordPath, "\\Record\\" );
}

////////////////////外部函数,为外通道设置与其相联的内通道
//------------------外部调用函数--辅助性-------------------------

//得到通道数量
int CLaneTel::GetChannelsNum ()	
{ 
	return m_iUseLineNum;
}

//得到某一条通道的状态

void CLaneTel::GetLineState ( ChannelStruct *pChanStruct, WORD wChannelNo )
{
	pChanStruct->wChannelNo = m_pChannels[wChannelNo]->GetChannelNo ();
	pChanStruct->iType 		= m_pChannels[wChannelNo]->GetChannelType (); //线路状态
	pChanStruct->iState		= m_pChannels[wChannelNo]->GetChannelState ();
	
	char temp[128];
	m_pChannels[wChannelNo]->GetCallerID ( temp );
	strcpy ( pChanStruct->sCallerID, temp );
	m_pChannels[wChannelNo]->GetRecordFileName ( temp );
	strcpy ( pChanStruct->sNowRecordFileName, temp );
}

//-----------------主要功能函数-------------------------

//建立一个对象后，要调用InitSystem()，才能进行别的操作
bool CLaneTel::InitSystem ( )
{
	long DriverOpenFlag;	//用于检测返回值

	GetVoicePath ();	//得到声音的路径。
	GetRecordPath ();	//得到录音的录音。
	GetRecFaxPath ();

	//设置在系统文件Tc08a-v.ini中的声音格式，WaveFormat=2，使用WAVE语音格式（线性 PCM 8000Hz，8位，单声道）
	char	sFileName[100];
	GetWindowsDirectory ( sFileName, 100 );
	strcat ( sFileName, "\\tc08a-v.ini" );
	
	CIniFile WavFormatConfig;
	WavFormatConfig.Create ( sFileName );
	WavFormatConfig.SetVarInt ( "D160A", "WaveFormat", 2 );

	DriverOpenFlag = ::LoadDRV ();	//加载电话卡驱动程序
	if ( DriverOpenFlag ) {
		::ShowError ( "打开设备驱动程序错误---LoadDRV()", "加载驱动程序失败" );
		return false;
	}

	//初始化电话卡的硬件并为每个通道分配语音缓冲区。
	m_iTotalLine = ::CheckValidCh();
	if ( ::EnableCard ( m_iTotalLine, 1024*48 ) != (long) 0 ) {
		::FreeDRV ();
		::ShowError ( "初始化电话卡的硬件失败---EnableCard()", "设备初始化失败" );
		return false;
	}

	::SetBusyPara(350);		//设定要检测的挂机忙音的参数，比如：国标中规定的0.7秒忙音信号，写为SetBusyPara(700)；

	//初始化传真通道
	if ( ::DJFax_DriverReady(2048) ) {
		::ShowError ( "加载传真设备失败---DJFax_DriverReady(2048)", "传真初始化失败" );
		//::DisableCard();
		//::FreeDRV();
		//return false;
	}
	
	CIniFile iniFile;
	iniFile.Create ( "config.ini" );

	//建立传真通道类型对象
	iniFile.GetVarInt ( "Fax", "OutLineNOWithFax", m_iFaxLineNo );
	if ( (m_iFaxLineNo <= m_iTotalLine-1) && (m_iFaxLineNo >= 0) &&
		::CheckChTypeNew(m_iFaxLineNo) == CHTYPE_TRUNK ) {
		m_pFaxChannel = new COutChannelWithFax ( m_iFaxLineNo );
		m_bUseFax		= true;
	}
	else {
		m_bUseFax		= false;
		m_pFaxChannel = NULL;
	}
	
	//建立外线通道类型对象		
	iniFile.GetVarInt ( "Telephone", "InLineNum", m_iUseInLineNum );
	iniFile.GetVarInt ( "Telephone", "OutLineNO", m_iOutLineNo );
	m_iUseLineNum = m_iUseInLineNum + 1;
	
	if ( ::CheckChTypeNew(m_iOutLineNo) != CHTYPE_TRUNK ) {
		if ( m_bUseFax ) {
			delete m_pFaxChannel;
		}
		::DJFax_DisableCard();
		::DisableCard ();	//关闭电话卡的硬件，释放缓冲区。程序结束(包括正常和不正常退出)时需调用此函数。
		::FreeDRV ();		//关闭驱动程序。
		::ShowError ( "请您设置正确的外线通道号", "您设置的要使用的外线通道号错误" );
		return false;
	}
	
	m_pChannels[0] = new COutChannel( m_iOutLineNo );

	//建立内线类型通道对象
	CString	sTemp;
	int iInLineNo;
	for( int i = 1; i <= m_iUseInLineNum; i ++ ) {
		sTemp.Format( "InLine%d", i );
		iniFile.GetVarInt ( "Telephone", sTemp, iInLineNo );
		if ( (::CheckChTypeNew(iInLineNo) != CHTYPE_USER) 
							|| iInLineNo > m_iTotalLine-1 || iInLineNo < 0 ) {
			if ( m_bUseFax ) {
				delete m_pFaxChannel;
			}
			delete m_pChannels[0];
			::DJFax_DisableCard();
			::DisableCard ();
			::FreeDRV ();	
			::ShowError ( "请设置正确的内线通道号", "您设置的要使用的内线通道号错误" );
			return false;
		}
	}

	for( int j = 1; j <= m_iUseInLineNum; j ++ ) {
		sTemp.Format( "InLine%d", j );
		iniFile.GetVarInt ( "Telephone", sTemp, iInLineNo );
		m_pChannels[j] = new CInChannel( iInLineNo );
	}
	
	//设置播放的声音和留言存放的路径
	CChannel::SetVoicePath( m_sVoicePath );	//设置要播放的文件路径
	CChannel::SetRecordPath ( m_sRecordPath );	//设置要录制的文件路径
	COutChannelWithFax::SetRecFaxPath ( m_sRecFaxPath );	//设置要接受的传真文件路径

	//设定内线的忙音文件
	char sInLineSig[128];
	strcpy ( sInLineSig, m_sVoicePath );
	strcat ( sInLineSig, "inline_sig.wav" );
	if ( !::ReadGenerateSigBuf ( sInLineSig ) ) {	
		::ShowError ( "::ReadGenerateSigBuf", "error" );
	}
	
	::Sig_Init(0);	//开始检测信号


	return true;
}

//程序结束时要释放设备
void CLaneTel::ExitSystem ( )
{
	::DJFax_DisableCard();//关闭传真卡
	
	::DisableCard ();	//关闭电话卡的硬件，释放缓冲区。程序结束(包括正常和不正常退出)时需调用此函数。
	::FreeDRV ();		//关闭驱动程序。
	
	//删除内线，外线对象
	for( int i = 0; i < m_iUseLineNum; i ++ ) {
		delete m_pChannels[i];
		m_pChannels[i] = NULL;
	}
	
	if ( m_bUseFax ) {
		delete m_pFaxChannel;	//删除传真通道对象
	}


}

//电话过程函数
void CLaneTel::TelProc ( )
{
	static	LinkInfo linkinfo;
	static	int	wLinkInPos;	//要连接的内线在数组中的位置
	int ret;

	PUSH_PLAY ();
	FeedSigFunc ();
	
	//--------------外线处理-------------------------
	
	ret = m_pChannels[0]->ChannelProc();
	
	if ( ret == OutReturn_LinkInLine ) {				//如果要连接内线

		m_pChannels[0]->GetLinkInfo ( &linkinfo );		//获得连接信息

		//发送网络消息~~~~~~~~~~~~~~~~~send ( hostname, callerid );
		SendMsg( linkinfo.sHostName );
		//检索所要连接的内线，并测试内线是否可用，
		//可用的话则设置相关信息
		for ( int j = 1; j <= m_iUseInLineNum; j ++ ) {	
			
			if ( linkinfo.wInLineNo == m_pChannels[j]->GetChannelNo() ) {	//找到要连接的内线
				
				wLinkInPos = j;
			
				if ( m_pChannels[j]->GetChannelState() == CH_FREE ) {		//该内线在空闲的状态下
					m_pChannels[j]->SetChannelState ( CH_RINGING );			//内线进入振铃状态
				}
				
				else {		//内线忙
					m_pChannels[0]->SetChannelState ( CH_INLINE_BUSY );		//外线进入内线忙状态
				}
			}
		}
	}

	else if ( ret == OutReturn_HangUp ) {
		m_pChannels[wLinkInPos]->SetChannelState ( CH_OUT_HANGUP );	//内线设为 外线挂机状态
		::ClearLink ( m_pChannels[0]->GetChannelNo(), linkinfo.wInLineNo );
	}


	//--------------内线处理-------------------------
	for ( int i = 1; i <= m_iUseInLineNum; i ++ ) {
		
		ret = m_pChannels[i]->ChannelProc();
		
		if ( ret == InReturn_FeedOffHook ) {	//内线已经摘机，可以连接两条线路
		
			//连接两条线
			if ( ::SetLink ( m_pChannels[0]->GetChannelNo(), linkinfo.wInLineNo ) == 0 ) {	//连接成功
				m_pChannels[i]->SetChannelState( CH_TALKING_WITH_OUT );
				m_pChannels[0]->SetChannelState( CH_TALKING_WITH_IN );
			}
			else {	//连接失败
				m_pChannels[i]->SetChannelState( CH_NO_LISTEN );
				m_pChannels[0]->SetChannelState( CH_INLINE_BUSY );
			}
		}
		
		else if ( ret == InReturn_NoListen ) {	//内线无人接听
			m_pChannels[0]->SetChannelState( CH_INLINE_HANGUP );
		}
		
		else if ( ret == InReturn_HangUp ) {	//内线已经挂机了
			m_pChannels[0]->SetChannelState( CH_INLINE_HANGUP );
			::ClearLink ( m_pChannels[0]->GetChannelNo(), linkinfo.wInLineNo );
		}
	}
}

//传真的过程函数
void CLaneTel::FaxProc()
{
	if ( m_bUseFax ) {
		m_pFaxChannel->ChannelProc();
	}
}

bool CLaneTel::IsUseFax() const
{
	return m_bUseFax;
}

void CLaneTel::GetRecFaxPath()
{
	GetCurrentDirectory ( 100, m_sRecFaxPath );
	strcat ( m_sRecFaxPath, "\\RecFax\\" );
}

void CLaneTel::GetFaxChnlState(FaxChnlStruct *pFaxStruct)
{
	pFaxStruct->wChannelNo = m_pFaxChannel->GetChannelNo ();
	pFaxStruct->iType 		= m_pFaxChannel->GetChannelType (); //线路状态
	pFaxStruct->iState		= m_pFaxChannel->GetChannelState ();
	
	char temp[128];
	m_pFaxChannel->GetCallerID ( temp );
	strcpy ( pFaxStruct->sCallerID, temp );
	m_pFaxChannel->GetRecFaxFileName ( temp );
	strcpy ( pFaxStruct->sNowRecFaxName, temp );
}

void CLaneTel::SendFax(char *sDialNo, char *sFaxName)
{
	m_pFaxChannel->SendFax ( sDialNo, sFaxName );
}

void CLaneTel::SendMsg(CString sHostName)
{
	SOCKADDR_IN    ClientAddr;
	int pos;
	if(!OnLIneInfoQueue.SearchItemByUserName(sHostName,&pos))
		return;
	ClientAddr.sin_family = AF_INET;
    ClientAddr.sin_port = htons(OnLIneInfoQueue[pos].GetListenPort());
    ClientAddr.sin_addr.s_addr = inet_addr(OnLIneInfoQueue[pos].GetIP());
	
	sendto(ListenSock, "3009", 4, 0,(SOCKADDR *) &ClientAddr, sizeof(ClientAddr));
	
}
