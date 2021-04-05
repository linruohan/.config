#ifndef	LANE_CHANNEL_H
#define	LANE_CHANNEL_H

#include "NewSig.h"
#include "Tc08a32.h"
#include "Conf95.h"
#include "Faxapi32.h"
#include "LaneTelDefine.h"

#include "LaneSpeech.h"
#include "Resource.h"
#include "namelist.h"	// Added by ClassView
/*//////////基类////////////////////////////////////////*/
class CChannel
{
public:
	CChannel( WORD wChanNo, int iType, int iState );
	virtual ~CChannel() { return; } ;

	static void SetVoicePath ( char * szVoicePath );//设置声音的路径
	static void SetRecordPath ( char *szRecordPath );

	virtual int ChannelProc() = 0;					//通道过程函数

	void SetChannelState ( CHANNEL_STATE state );	//设置本通道的状态
	int  GetChannelState ( ) const;					//获得本通道的状态

	WORD GetChannelNo ( ) const;					//获得本通道的通道编号
	int GetChannelType () const;					//获得通道类型
	
	virtual void GetRecordFileName ( char * szFileName ) = 0;
	virtual void GetCallerID ( char *szCallerID ) = 0;
	virtual void GetLinkInfo ( LinkInfo * pLinkInfo ) = 0;
protected:
	void PlayWavFile ( char *szFileName );	//在本通道播放线性pcm文件
	
	static	char m_sVoicePath[100];				//要播放的声音的路径
	static char m_sRecordPath[100];

	virtual void ResetChannel() = 0;			//重新初始化本通道
	inline char DtmfToChar( short int ch );		//转换函数
	
protected:
	WORD		m_wChannelNo;			//通道号
	int			m_iType;				//通道类型
	int			m_iState;				//通道状态
	char		m_sDtmf[32];			//按键缓冲
	int			m_iTimeElapse;			//流逝时间
};

/*//////////外线////////////////////////////////////////*/
class COutChannel : public CChannel	//外线。
{
public:
	COutChannel( WORD wChanNo, int iType = CHTYPE_TRUNK, int iState = CH_FREE );
	virtual ~COutChannel();
	virtual int ChannelProc();
	virtual void GetRecordFileName ( char * szFileName );
	virtual void GetCallerID ( char *szCallerID );
	
protected:
	virtual void ResetChannel();

	void GetLinkInfo ( LinkInfo * pLinkInfo );
	void RecordWavFile ( char *szFullFileName, DWORD dwFileLen, DWORD dwRecordStartPos = 0L );
	void ComputCallerID();
	//留言相关
	int			m_iRecordFileName;	//用于计算当前录音的文件名
	void		ComputRecordFileName ();	//计算当前录音的文件名
	
protected:
	CNameList	m_NameList;
	char		m_sCallerID[32];			//来电ID
	char		m_sNowRecordFileName[128];	//当前录音的文件名
	char		m_szSRWaveFile[28];			//用于向外部显示
	wchar_t		m_wzSRWaveFile[28];			//用于向引擎输入
	CSR			*m_pSR;						//SR指针
	LinkInfo	m_LinkInfo;					//线路相关的信息，主要用于向外传播信息
};

/*//////////内线////////////////////////////////////////*/
class CInChannel : public CChannel
{
public:
	CInChannel( WORD wChanNo, int iType = CHTYPE_USER, int iState = CH_FREE );
	virtual ~CInChannel() { return; };
	virtual int ChannelProc();
	virtual void GetRecordFileName ( char * szFileName ){ strcpy ( szFileName, "" ); };
	virtual void GetCallerID ( char *szCallerID ){  strcpy ( szCallerID, "" );  };
	virtual void GetLinkInfo ( LinkInfo * pLinkInfo ) {};
protected:
	virtual void ResetChannel();
};

/*//////////悬空////////////////////////////////////////*/
class CEmptyChannel : public CChannel
{
public:
	CEmptyChannel( WORD wChanNo, int iType = CHTYPE_EMPTY, int iState = CH_EMPTY ) : CChannel( wChanNo, iType, iState ) { return; }
	virtual ~CEmptyChannel() { return; };
	virtual int ChannelProc() { return OutReturn_Nothing; };
	virtual void GetRecordFileName ( char * szFileName ){ strcpy ( szFileName, "" ); };
	virtual void GetCallerID ( char *szCallerID ){  strcpy ( szCallerID, "" );  };
	virtual void GetLinkInfo ( LinkInfo * pLinkInfo ) {};
protected:
	virtual void ResetChannel() { return; };
};


class COutChannelWithFax : public COutChannel  
{
public:
	void GetRecFaxFileName ( char * psRecFaxFile );
	static void SetRecFaxPath( char *psRecFaxPath );
	void SendFax ( char * psDialNo, char * psFaxFileName );
	virtual void ResetChannel();
	virtual int ChannelProc();
	COutChannelWithFax( WORD wChanNo, int iType = CHTYPE_TRUNK_WITH_FAX, int iState = CH_FREE );
	virtual ~COutChannelWithFax();


protected:
	void ComputRecFaxName();
	static char m_sRecFilePath[100];
	char m_sNowRecFaxName[128];
	char m_sDialNo[28];
	char m_sSendFileName[256];
	WORD m_wFaxChannelNo;		//传真通道号
};

#endif	//	LANE_CHANNEL_H