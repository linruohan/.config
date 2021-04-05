#include "stdAfx.h"
#include "LaneChannel.h"
#include "CLog.h"

#pragma  comment (lib,"TC08A32.LIB")
#pragma  comment (lib,"NewSig.LIB")
#pragma  comment (lib,"Speech_Re.lib")

#ifdef _DEBUG
#undef THIS_FILE
static char THIS_FILE[]=__FILE__;
#define new DEBUG_NEW
#endif



//通道的构造函数
CChannel::CChannel ( WORD wChanNo, int iType, int iState )
{
	m_wChannelNo	= wChanNo;
	m_iType			= iType;
	m_iState		= iState;
	m_sDtmf[0]		= 0;
	m_iTimeElapse	= 0;
}

//把Dtmf代码转化成字符
inline char CChannel::DtmfToChar( short int ch )
{
	char c;
	switch(ch)
    {
		case 10:
			c = '0';
			break;
		case 11:
			c = '*';
			break;
		case 12:
			c = '#';
			break;
        case 13:
        case 14:
        case 15:
            c=ch-13+'a';
            break;
        case 0:
            c='d';
            break;
		default:
			c = ch + '0';	//change DTMF from number to ASCII
	}
	return c;
}

//播放wav文件
void CChannel::PlayWavFile ( char *szFileName )
{
	char temp[128];
	strcpy ( temp, m_sVoicePath );
	strcat ( temp, szFileName );
	::StartPlayFile ( m_wChannelNo, temp, 0L );
}

//设置声音的路径
void CChannel::SetVoicePath ( char *szVoicePath )
{
	strcpy ( m_sVoicePath, szVoicePath );
}

//设置留言文件放置的路径
void CChannel::SetRecordPath ( char * szRecordPath )
{
	strcpy ( m_sRecordPath, szRecordPath );
}

//设置本通道的状态
void CChannel::SetChannelState ( CHANNEL_STATE state )
{
	m_iState = state;		
}
	
//获得本通道的状态
int  CChannel::GetChannelState ( ) const
{
	return m_iState;
}

//获得本通道的通道号
WORD CChannel::GetChannelNo ( )	const	
{
	return m_wChannelNo;
}

//获得本通道类型
int CChannel::GetChannelType () const
{
	return m_iType;
}

//外线的构造函数
COutChannel::COutChannel( WORD wChanNo, int iType, int iState ) : CChannel( wChanNo, iType, iState )
{
	m_sCallerID[0] = 0;
	m_sNowRecordFileName[0] = 0;
	::InitDtmfBuf ( m_wChannelNo );	//清空Dtmf缓冲
	m_iRecordFileName = 1;

	char temp[28];
	sprintf ( temp, "sr%d.wav", wChanNo );
	strcpy ( m_szSRWaveFile, temp );
	
	MultiByteToWideChar ( CP_ACP, //把char转换成wchar_t
						  0,
						  m_szSRWaveFile,
						  sizeof(m_szSRWaveFile)/sizeof(char),
						  m_wzSRWaveFile,
						  28 * sizeof( wchar_t ) );
	
	m_pSR = new CSR;
	m_pSR->Create();	//初始化SR
	m_pSR->LoadCrammarFile( L"grammar.xml" );

	::StartSigCheck ( m_wChannelNo );				//某路开始新的信号音检测。
}

//外线的析构函数
COutChannel::~COutChannel ( )
{
	delete m_pSR;
	m_pSR = NULL;
}

//获得i通道的主叫号码
void COutChannel::ComputCallerID ( )
{
	short int code;
	int i = 0;
	code = ::GetDtmfCode( m_wChannelNo );
	
	if ( code == -1 ) {	//如果缓冲中没有Dtmf，则收不到主叫号码
		strcpy ( m_sCallerID, "Can't Get CallerID" );
		return;
	}
	while ( code != -1 ) {
		m_sCallerID[i++] = DtmfToChar ( code );
		code = ::GetDtmfCode( m_wChannelNo );	
	}
}

//支持传真的外线的过程函数
int COutChannel::ChannelProc ( )
{
	static int i;
	short int code;
	char RecoName[64];
	char sTemp[10][128];
	
	switch ( m_iState ) {	
		
		case CH_FREE:			//空闲状态
			if ( ::RingDetect ( m_wChannelNo ) ) {	//有振铃？
				ComputCallerID ();					//获得来电的电话号码
				::OffHook ( m_wChannelNo );			//摘机
				m_iState = CH_OFFHOOK;
			}
			break;
		
		case CH_OFFHOOK:		//摘机状态
			PlayWavFile ( "welcome.wav" );	//播放“这里是某某电话系统”
			m_iState = CH_WELCOME;
		
		case CH_WELCOME:		//欢迎状态，播放主菜单
			code = ::GetDtmfCode ( m_wChannelNo );
			if ( ( code != -1 ) || ::CheckPlayEnd ( m_wChannelNo ) ) {
				::StopPlayFile ( m_wChannelNo );
				PlayWavFile ( "select.wav" );//应该播放主菜单选项？“语音找人按1，按键找人按2，留言按3，发传真按4”
				m_iState = CH_SELECT;
			}
			break;
		
		case CH_SELECT:			//主菜单状态
			code = ::GetDtmfCode ( m_wChannelNo );
			if ( code != -1 ) {
				m_sDtmf[0] = DtmfToChar ( code );
				m_sDtmf[1] = 0;
				switch ( m_sDtmf[0] ) {
					case '1':	//根据语音找人
						::StopPlayFile ( m_wChannelNo );
						PlayWavFile ( "speech_start.wav" );//播放“请说出你要找的人的名字,按#键结束”
						m_iState = CH_CALL_BY_SPEECH_START;	//转换到识别人名状态//！！！！！！！！！！
						break;
					case '2':	//根据按键找人
						::StopPlayFile ( m_wChannelNo );
						PlayWavFile ( "dtmf_start.wav" );//播放“请按您要找的人的按键码，按#号结束”	
						m_iState = CH_CALL_BY_DTMF_START;
						break;
					case '3':	//留言
						::StopPlayFile ( m_wChannelNo );
						PlayWavFile ( "message_start.wav" );//播放“听到嘟的一声后请说出留言，按#号结束。嘟!!”	
						m_iState = CH_RECORD_MESSAGE_START;
						break;
					//case '4':	//发传真???????????????????????
					//	::StopPlayFile ( m_wChannelNo );
					//	PlayWavFile ( "message_start.wav" );//播放“听到嘟的一声后请说出留言，按#号结束。嘟!!”	
					//	m_iState = CH_RECORD_MESSAGE_START;
					//	break;
					default:	//重新播放选择菜单的声音
						if ( ::CheckPlayEnd ( m_wChannelNo ) ) {
							::StopPlayFile ( m_wChannelNo );
							m_iState = CH_WELCOME;
						}
						break;
				}//end 子switch
			}//if
			break;
			
	
/////////////////////////////////////////////////////
//-------------留言模块		
		case CH_RECORD_MESSAGE_START:	//开始录制留言
			code = ::GetDtmfCode ( m_wChannelNo );
			if ( ::CheckPlayEnd(m_wChannelNo) || code != -1 ) {
				::StopPlayFile ( m_wChannelNo );
				ComputRecordFileName ();	//计算出要存储的文件名
				RecordWavFile ( m_sNowRecordFileName, 240058, 0L );//对本通道进行30秒的录音
				m_iState = CH_RECORD_MESSAGE_ING;
			}
			break;
		
		case CH_RECORD_MESSAGE_ING:	//正在录制留言
			code = ::GetDtmfCode ( m_wChannelNo );
			if ( ::CheckRecordEnd( m_wChannelNo ) || ( DtmfToChar(code)=='#') ) {
				::StopRecordFile ( m_wChannelNo );//停止录音（写数据到文件）
				PlayWavFile ( "message_end.wav" );	//播放“留言结束”
				m_iState = CH_RECORD_MESSAGE_END;	
			}
			break;
		
		case CH_RECORD_MESSAGE_END:	//录制留言结束
			if ( ::CheckPlayEnd ( m_wChannelNo ) ) {
				::StopPlayFile ( m_wChannelNo );
				m_iState = CH_WELCOME;	//回到欢迎状态，（播放主菜单）
			}
			break;
			
			
/////////////////////////////////////////////////////
//-------------按键找人模块			
		
		case CH_CALL_BY_DTMF_START:		//开始接受输入识别人的DTMF
			code = ::GetDtmfCode ( m_wChannelNo );
			if ( (code != -1) || ::CheckPlayEnd(m_wChannelNo) ) {
				::StopPlayFile ( m_wChannelNo );
				m_sDtmf[0] = DtmfToChar( code );
				i = 1;
				m_iState = CH_CALL_BY_DTMF_GETDTMF;

			}
			break;
		
		case CH_CALL_BY_DTMF_GETDTMF:	//正在接受输入识别人的DTMF
			code = ::GetDtmfCode ( m_wChannelNo );
			if ( code != -1 ) {
				m_sDtmf[i] = DtmfToChar( code );
				if ( m_sDtmf[i] == '#' ) {
					m_sDtmf[i+1] = 0;
					m_iState = CH_CALL_BY_DTMF_SEARCHING;
		
				}
				i ++;
				if ( i>30 ) {
					ResetChannel ();
				}
			}
			break;
			
		case CH_CALL_BY_DTMF_SEARCHING:	{	//根据按键码查找数据库
			int k = m_NameList.GetHostByDtmf ( m_sDtmf, sTemp, 1 );
			if ( k != 0 ) {	//找到了			
				m_NameList.GetInLineNoByHost( sTemp[0] );
				m_LinkInfo.wInLineNo = m_NameList.GetInLineNoByHost( sTemp[0] );
				m_LinkInfo.sHostName = sTemp[0];
				m_LinkInfo.sCallerID = m_sCallerID;
				m_iState = CH_WAIT_LINK;
				return OutReturn_LinkInLine;
			}
			else {			//没找到匹配的人名
				PlayWavFile ( "search_fail.wav" );	//播放“没找到您要找的人”
				m_iState = CH_WELCOME;
			}
			
		}
			break;	
/////////////////////////////////////////////////////
//-------------语音找人模块	
		
		case CH_CALL_BY_SPEECH_START:	//语音模块开始
			code = ::GetDtmfCode ( m_wChannelNo );
			if ( ::CheckPlayEnd(m_wChannelNo) || code != -1 ) {
				::StopPlayFile ( m_wChannelNo );

				RecordWavFile ( m_szSRWaveFile, 80058, 0L );//对i通道进行10秒的录音


				m_iState = CH_CALL_BY_SPEECH_RECORDING; //转换到识别状态
			}
			break;
			
		case CH_CALL_BY_SPEECH_RECORDING:	//正在录音
			code = ::GetDtmfCode ( m_wChannelNo );
			
			if ( ::CheckRecordEnd( m_wChannelNo ) || DtmfToChar(code) == '#' ) { //录音结束

				::StopRecordFile ( m_wChannelNo );	//停止录音（写数据到文件）
				m_iState = CH_CALL_BY_SPEECH_RECONITION;
			}
			break;
		
		case CH_CALL_BY_SPEECH_RECONITION:	//识别状态
			m_pSR->SetInputFromWav( m_wzSRWaveFile, SPSF_8kHz8BitMono );
			m_pSR->StartReco();
			m_pSR->ProcessReco();
			if ( m_pSR->IsRecoSuccess() && m_pSR->IsRecoEnd() ) {
				m_pSR->GetRecoWordA( RecoName );
				int k = m_NameList.GetHostByName ( RecoName, sTemp, 1 );
				if ( k != 0 ) {	//找到了			
					m_LinkInfo.sHostName = sTemp[0];
					m_NameList.GetInLineNoByHost( sTemp[0] );
					m_LinkInfo.wInLineNo = m_NameList.GetInLineNoByHost( sTemp[0] );
					m_LinkInfo.sCallerID	 = m_sCallerID;
					m_iState = CH_WAIT_LINK;

					return OutReturn_LinkInLine;
				}
				else {			//没找到匹配的人名
					PlayWavFile ( "search_fail.wav" );	//播放“没找到您要找的人”
					m_iState = CH_WELCOME;

				}
			}
			else {	//识别失败，回到主菜单的状态
				PlayWavFile ( "search_fail.wav" );	//播放“没找到您要找的人”
				m_iState = CH_WELCOME;

			}
			break;
		
/////////////////////////////////////////////////////
//-------------与内线通话相关

		case CH_WAIT_LINK:	//等待与内线相连
			::StopPlayFile ( m_wChannelNo );
			if ( ::Sig_CheckBusy ( m_wChannelNo ) == 1 ) {	//有忙音，对方已挂机
				ResetChannel ();
				return OutReturn_HangUp;
			}

			break;

		case CH_INLINE_BUSY:		//内线忙
			PlayWavFile ( "inline_busy.wav" );	//播放“内线忙”
			m_iState = CH_WELCOME;

			break;

		case CH_INLINE_HANGUP:		//通话中内线挂机
			ResetChannel ( );
			m_iState = CH_FREE;

			break;

		case CH_TALKING_WITH_IN:	//正在与内线通话
			if ( ::Sig_CheckBusy ( m_wChannelNo ) == 1 ) {	//有忙音，对方已挂机
				ResetChannel ();

				return OutReturn_HangUp;
			}
			break;

/////////////////////////////////////////////////////
//-------------传真模块			
		
	}	//end switch
	
	//检查是否半截挂机！！！
	if( m_iState != CH_FREE ) {
		if ( ::Sig_CheckBusy ( m_wChannelNo ) == 1 ) {
			switch ( m_iState )
			{
	        	case CH_OFFHOOK:
	        	case CH_WELCOME:
				case CH_SELECT:
				case CH_RECORD_MESSAGE_END:
				case CH_CALL_BY_DTMF_START:
				case CH_CALL_BY_DTMF_SEARCHING:
				case CH_CALL_BY_SPEECH_RECONITION:
				case CH_INLINE_BUSY:
				case CH_INLINE_HANGUP:
					::StopPlayFile ( m_wChannelNo );
					break;
				
				case CH_RECORD_MESSAGE_START:
				case CH_RECORD_MESSAGE_ING:
				case CH_CALL_BY_SPEECH_START:
					::StopPlayFile ( m_wChannelNo );
					::StopRecordFile ( m_wChannelNo );
					break;
				
				case CH_CALL_BY_SPEECH_RECORDING:
					::StopRecordFile ( m_wChannelNo );
					break;

				case CH_WAIT_LINK:
				case CH_TALKING_WITH_IN:	//正在与内线通话
					::StopRecordFile ( m_wChannelNo );
					return OutReturn_HangUp;
					break;
			}
			//return OutReturn_HangUp;
			ResetChannel ();
		}
	}
	return OutReturn_Nothing;
	
}

//重新初始化通道
void COutChannel::ResetChannel ( )
{
	::HangUp ( m_wChannelNo );						//外线挂机，对于内线，此函数不起作用。
	::Sig_ResetCheck ( m_wChannelNo );				//清空忙音检测的缓冲区以及内部计数。当检测对方挂机的忙音后，必须调用本函数。
	::StartSigCheck ( m_wChannelNo );				//某路开始新的信号音检测。一般在摘机或者挂机后，调用本函数来开始新的信号音检测。
		
	::InitDtmfBuf ( m_wChannelNo );	//清空Dtmf缓冲
		
	m_sDtmf[0] = 0;
	m_sCallerID[0] = 0;
	m_iState = CH_FREE;
}

//录制声音到线性Wav文件，每秒占8000字节，最后还要加上58字节的文件头
void COutChannel::RecordWavFile ( char *szFullFileName, DWORD dwFileLen, DWORD dwRecordStartPos )
{
	::StartRecordFileNew ( m_wChannelNo, szFullFileName, dwFileLen, dwRecordStartPos );
}

//计算当前录音的文件名，一共存放10个文件，轮换着存储。
void COutChannel::ComputRecordFileName ()
{
	char temp[28];
	m_iRecordFileName %= 10;	//文件名 0~9.wav
	sprintf ( temp, "%d.wav", m_iRecordFileName );
	strcpy ( m_sNowRecordFileName, m_sRecordPath );
	strcat ( m_sNowRecordFileName, temp );
	m_iRecordFileName ++;
}

//对外界送出当前录音的文件名
void COutChannel::GetRecordFileName ( char * szFileName )
{
	strcpy ( szFileName, m_sNowRecordFileName );
}

//对外界显示当前的来电号码
void COutChannel::GetCallerID ( char *szCallerID )
{
	strcpy ( szCallerID, m_sCallerID );
}

//获得要连接的内线的信息
void COutChannel::GetLinkInfo(LinkInfo *pLinkInfo)
{
	pLinkInfo->sHostName = m_LinkInfo.sHostName;
	pLinkInfo->wInLineNo = m_LinkInfo.wInLineNo;
	pLinkInfo->sCallerID = m_LinkInfo.sCallerID;
}

//内线构造函数
CInChannel::CInChannel( WORD wChanNo, int iType, int iState ) : CChannel( wChanNo, iType, iState )
{
	::InitDtmfBuf ( m_wChannelNo );	//清空Dtmf缓冲
}

//内线过程函数
int CInChannel::ChannelProc ( )
{
	short int code;
	char sRecordFile[2];			//存储由按键得到的录音文件名序号
	static char sTemp[128];
	
	switch (  m_iState ) {
		case CH_FREE:				//空闲状态
			if ( ::RingDetect ( m_wChannelNo ) ) {
				m_iState = CH_OFFHOOK;
			}
			break;
	
		case CH_OFFHOOK:			//内线摘机
			code = ::GetDtmfCode ( m_wChannelNo );
			if ( code != -1 ) {
				if ( DtmfToChar ( code ) == '#' ) {
					m_iState = CH_CHOICE_MESSAGE;
				}
			}
			break;

////////////////////////////////////////////////////////////	
/////////-----------听留言----------------------------------
		case CH_CHOICE_MESSAGE:		//选择要听的留言
			code = ::GetDtmfCode ( m_wChannelNo );
			if ( code != -1 ) {
				sRecordFile[0] = DtmfToChar ( code );
				sRecordFile[1] = 0;
				strcpy ( sTemp, m_sRecordPath );
				strcat ( sTemp, sRecordFile );
				strcat ( sTemp, ".wav" );
				m_iState = CH_PLAY_MESSAGE_START;
			}
			break;
		
		case CH_PLAY_MESSAGE_START:	//开始播放留言
			::StartPlayFile ( m_wChannelNo, sTemp, 0L );
			m_iState = CH_PLAY_MESSAGE_ING;
			break;
		
		case CH_PLAY_MESSAGE_ING:	//正在播放留言
			code = ::GetDtmfCode ( m_wChannelNo );
			if ( ( code != -1 ) || ::CheckPlayEnd ( m_wChannelNo ) ) {
				::StopPlayFile ( m_wChannelNo );
				m_iState = CH_PLAY_MESSAGE_END;
			}
			break;
		
		case CH_PLAY_MESSAGE_END:	//留言播放结束
			m_iState = CH_OFFHOOK;
			break;

////////////////////////////////////////////////////////////
/////////-----------与外线连通相关----------------------------------
		case CH_RINGING:			//响铃状态
			::FeedRealRing ( m_wChannelNo );
			::StartTimer ( m_wChannelNo, 5 );

			m_iState = CH_WAIT_OFFHOOK;

			break;

		case CH_WAIT_OFFHOOK:		//等待内线摘机状态

			if ( ::OffHookDetect ( m_wChannelNo ) == 1 ) {	//已经摘机
				::FeedPower ( m_wChannelNo );	//停止振铃
				m_iState = CH_FEED_OFFHOOK;	

			}
			else {					//检查是否超过一定时间（30秒）没人接电话
				if ( ::ElapseTime ( m_wChannelNo, 5 ) >= 3000 ) {	
					::FeedPower ( m_wChannelNo );	//停止振铃
					m_iState = CH_NO_LISTEN;

				}
			}
			break;
		
		case CH_NO_LISTEN:			//没人接听状态
			m_iState = CH_FREE;

			return InReturn_NoListen;
			break;

		case CH_FEED_OFFHOOK:		//要与外线连通情况下的摘机状态
			::StartHangUpDetect ( m_wChannelNo );	//有铃声后开始挂机检测
			m_iState = CH_WAIT_LINK;

			return InReturn_FeedOffHook;
			break;

		case CH_WAIT_LINK:			//等待与外线连通状态
			::StopPlayFile ( m_wChannelNo );
			if ( ::HangUpDetect ( m_wChannelNo ) == HANG_UP_FLAG_TRUE ) {	//如果半路挂机
				m_iState = CH_FREE;
				ResetChannel();

				return InReturn_HangUp;
			}
			break;

		case CH_TALKING_WITH_OUT:	//正在与外线通话状态。
			if ( ::HangUpDetect ( m_wChannelNo ) == HANG_UP_FLAG_TRUE ) {
				m_iState = CH_FREE;
				ResetChannel();

				return InReturn_HangUp;
			}
			break;

		case CH_OUT_HANGUP:			//外线已挂机
			::StartPlaySignal ( m_wChannelNo, SIG_BUSY1 );
			::FeedPower ( m_wChannelNo );	//停止振铃
			m_iState = CH_WAIT_IN_HANGUP;

			break;

		case CH_WAIT_IN_HANGUP:		//外线已挂机，等待内线挂机
			if ( ::HangUpDetect ( m_wChannelNo ) == HANG_UP_FLAG_START ) {
				::StartPlaySignal ( m_wChannelNo, SIG_STOP );
				m_iState = CH_FREE;
				ResetChannel ();

			}
			break;
	
	}	//end switch
	
	if ( (m_iState != CH_FREE) && (m_iState != CH_WAIT_OFFHOOK) && 
				( m_iState != CH_TALKING_WITH_OUT) ) {
		if( !::RingDetect ( m_wChannelNo ) ) {
			switch( m_iState )
			{
	            case CH_PLAY_MESSAGE_START:
				case CH_PLAY_MESSAGE_ING:
					::StopPlayFile ( m_wChannelNo );
					break;
				case CH_TALKING_WITH_OUT:
					::StopPlayFile ( m_wChannelNo );
					return InReturn_HangUp;
			}
			ResetChannel ();
		}
	}
	return InReturn_Nothing;
}

//重新初始化通道
void CInChannel::ResetChannel ( )
{
	::InitDtmfBuf ( m_wChannelNo );	//清空Dtmf缓冲
	::StartPlaySignal ( m_wChannelNo, SIG_STOP );
	m_sDtmf[0] = 0;
	m_iState = CH_FREE;
}

//////////////////////////////////////////////////////////////////////
// COutChannelWithFax Class----支持传真的外线通道类
//////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////
// Construction/Destruction
//////////////////////////////////////////////////////////////////////

COutChannelWithFax::COutChannelWithFax( WORD wChanNo, int iType, int iState ): COutChannel( wChanNo, iType, iState )
{

}

COutChannelWithFax::~COutChannelWithFax()
{

}

int COutChannelWithFax::ChannelProc()
{
	int ret;
	short int code;
	
	//char sTemp[10][128];
	
	switch ( m_iState ) {	
		
		case CH_FREE:			//空闲状态
			if ( ::RingDetect ( m_wChannelNo ) ) {	//有振铃？
				ComputCallerID ();					//获得来电的电话号码
				::OffHook ( m_wChannelNo );			//摘机
				m_iState = CH_OFFHOOK;
			}
			break;
		
		case CH_OFFHOOK:		//摘机状态
			PlayWavFile ( "welcome.wav" );	//播放“这里是某某电话系统”
			m_iState = CH_WELCOME;
		
		case CH_WELCOME:		//这里是东进电话银行演示系统
			code = ::GetDtmfCode ( m_wChannelNo );
			if ( ( code != -1 ) || ::CheckPlayEnd ( m_wChannelNo ) ) {
				::StopPlayFile ( m_wChannelNo );
				PlayWavFile ( "fax_select.wav" );//应该播放主菜单选项？“发传真请按一”
				m_iState = CH_SELECT;
			}
			break;
		
		case CH_SELECT:			//主菜单状态
			code = ::GetDtmfCode ( m_wChannelNo );
			if ( code != -1 ) {
				m_sDtmf[0] = DtmfToChar ( code );
				m_sDtmf[1] = 0;
				switch ( m_sDtmf[0] ) {
					case '1':	//发传真
						::StopPlayFile ( m_wChannelNo );
						//PlayWavFile ( "message_start.wav" );//播放“听到嘟的一声后请说出留言，按#号结束。嘟!!”	
						m_iState = CH_RECEIVE_FAX_LINK;
						break;
					
					default:	//重新播放选择菜单的声音
						if ( ::CheckPlayEnd ( m_wChannelNo ) ) {
							::StopPlayFile ( m_wChannelNo );
							m_iState = CH_WELCOME;
						}
						break;
				}//end 子switch
			}//if
			break;
/////////////////////////////////////////////////////
//-------------接收传真模块				
		case CH_RECEIVE_FAX_LINK:		//接收传真连接通道
			
			code = ::GetDtmfCode ( m_wChannelNo );
			if ( ( code != -1 ) || ::CheckPlayEnd ( m_wChannelNo ) ) {
				
				::StopPlayFile ( m_wChannelNo );
			
				ret = ::DJFax_GetOneFreeFaxChnl();	//尝试获得一个空闲的传真通道

				if ( ret == -1 ) {	//没有空闲的传真通道
					PlayWavFile ( "fax_Chnl_busy.wav" );//播放“传真通道忙”	
					m_iState = CH_WELCOME;
				}
			
				else {			//获得空闲的通道
					m_wFaxChannelNo = ( WORD ) ret;
					::StopPlayFile ( m_wChannelNo );
				
					if ( ::DJFax_SetLink( m_wFaxChannelNo, m_wChannelNo ) ) {	//连接成功
						m_iState = CH_RECEIVE_FAX_START;
					}
				
					else {
						PlayWavFile ( "link_fax_chnl_fail.wav" );//播放“连接传真系统失败”	
						m_iState = CH_WELCOME;
					}
				}
			}
			break;
		
		case CH_RECEIVE_FAX_START:			//接受传真 开始 状态
			ComputRecFaxName();
			ret = ::DJFax_RcvFaxFile ( m_wFaxChannelNo, m_sNowRecFaxName );
			if ( ret != 1 ) {	//接受错误
				::DJFax_StopFax ( m_wFaxChannelNo );
				::DJFax_ClearLink ( m_wFaxChannelNo, m_wChannelNo );
				PlayWavFile ( "send_fax_fail.wav" );//播放“发送失败”	
				m_iState = CH_WELCOME;
			}
			else {	//接受成功
				m_iState = CH_RECEIVE_FAX_ING;
			}
			break;

		case CH_RECEIVE_FAX_ING:		//正在接受传真
			ret = ::DJFax_CheckTransmit ( m_wFaxChannelNo );
			if ( ret == 1 ) {	//所有都接受完毕
				m_iState = CH_RECEIVE_FAX_END;
			}
			else if ( ret < 0 ) {	//接受错误
				::DJFax_StopFax ( m_wFaxChannelNo );
				::DJFax_ClearLink ( m_wFaxChannelNo, m_wChannelNo );
				PlayWavFile ( "send_fax_fail.wav" );//播放“发送失败”	
				m_iState = CH_WELCOME;
			}
			break;

		case CH_RECEIVE_FAX_END:		//传真接受结束
			::DJFax_StopFax ( m_wFaxChannelNo );
			::DJFax_ClearLink ( m_wFaxChannelNo, m_wChannelNo );
			PlayWavFile ( "send_fax_end.wav" );//播放“发送完成”	
			m_iState = CH_WELCOME;
			break;

/////////////////////////////////////////////////////
//-------------发送传真模块
		case CH_SEND_FAX_LINK:		//连接传真通道
			::StopPlayFile ( m_wChannelNo );
			
			ret = ::DJFax_GetOneFreeFaxChnl();	//尝试获得一个空闲的传真通道

			if ( ret == -1 ) {	//没有空闲的传真通道	
				m_iState = CH_FREE;
				
				return FaxReturn_NoFreeFaxCh;	//---------
			}
			
			else {			//获得空闲的通道
				m_wFaxChannelNo = ( WORD ) ret;
								
				if ( ::DJFax_SetLink( m_wFaxChannelNo, m_wChannelNo ) ) {	//连接成功
					m_iState = CH_SEND_FAX_DAIL;
				}
				
				else {
					m_iState = CH_FREE;
					return FaxReturn_LinkFail;
				}
			}
			break;

		case CH_SEND_FAX_DAIL:		//传真发送开始
			ret = ::DJFax_SetDialNo ( m_wFaxChannelNo, m_sDialNo );
			if ( ret == 1 ) {
				m_iState = CH_SEND_FAX_START;
			}
			else {
				ResetChannel();
				return FaxReturn_LinkFail;
			}
		
			break;
		
		case CH_SEND_FAX_START:		//传真发送开始
			ret = ::DJFax_SendFaxFile ( m_wFaxChannelNo, m_sSendFileName );
			switch ( ret ) {
				case -1:
				case -2:
				case -3:
				case -4:
					ResetChannel();
					return FaxReturn_SendFail;
					break;
				default:
					m_iState = CH_SEND_FAX_ING;
					break;
			}
			break;	
		
		case CH_SEND_FAX_ING:		//传真发送中
			ret = ::DJFax_CheckTransmit ( m_wFaxChannelNo );
			if ( ret == 1 ) {	//所有都接受完毕
				m_iState = CH_SEND_FAX_END;
			}
			else if ( ret < 0 ) {	//接受错误
				ResetChannel();
				return FaxReturn_SendFail;
			}
			break;
	
		case CH_SEND_FAX_END:		//传真发送结束
			ResetChannel();
			return FaxReturn_SendSuccess;
			break;
		
	}	//end switch
	
	//检查是否半截挂机！！！
	if( m_iState != CH_FREE ) {
		if ( ::Sig_CheckBusy ( m_wChannelNo ) == 1 ) {
			switch ( m_iState )
			{
	        	case CH_OFFHOOK:
	        	case CH_WELCOME:
				case CH_SELECT:
				
				case CH_RECEIVE_FAX_LINK:
				case CH_RECEIVE_FAX_START:
				case CH_RECEIVE_FAX_ING:
				case CH_RECEIVE_FAX_END:
					::StopPlayFile ( m_wChannelNo );
					break;
				
				case CH_SEND_FAX_LINK:
				case CH_SEND_FAX_DAIL:
				case CH_SEND_FAX_START:
				case CH_SEND_FAX_ING:
				case CH_SEND_FAX_END:
					break;
			}
			ResetChannel ();
		}
	}
	return OutReturn_Nothing;
}

void COutChannelWithFax::ResetChannel()
{
	::DJFax_StopFax ( m_wFaxChannelNo );
	::DJFax_ClearLink ( m_wFaxChannelNo, m_wChannelNo );
	m_iState = CH_FREE;
}

void COutChannelWithFax::SendFax(char *psDialNo, char *psFaxFileName)
{
	strcpy ( m_sDialNo, psDialNo );
	strcpy ( m_sSendFileName, psFaxFileName );
	m_iState = CH_SEND_FAX_LINK;
}

void COutChannelWithFax::SetRecFaxPath( char *psRecFaxPath )
{
	strcpy ( m_sRecFilePath, psRecFaxPath );
}

void COutChannelWithFax::ComputRecFaxName()
{
	char temp[28];
	m_iRecordFileName %= 100;	//文件名 0~9.wav
	sprintf ( temp, "%d.bfx", m_iRecordFileName );
	strcpy ( m_sNowRecFaxName, m_sRecFilePath );
	strcat ( m_sNowRecFaxName, temp );
	m_iRecordFileName ++;
}

void COutChannelWithFax::GetRecFaxFileName(char *psRecFaxFile)
{
	strcpy ( psRecFaxFile, m_sNowRecFaxName ); 
}

char CChannel::m_sVoicePath[100] = "";
char CChannel::m_sRecordPath[100] = "";
char COutChannelWithFax::m_sRecFilePath[100] = "";


