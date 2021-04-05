#ifndef LANE_TEL_H
#define LANE_TEL_H

#include "LaneChannel.h"

class CLaneTel
{

public:
	static void SendMsg ( CString sHostName );
	void SendFax( char * sDialNo, char * sFaxName );
	void GetFaxChnlState (  FaxChnlStruct * pFaxStruct );
	bool IsUseFax() const;
	void FaxProc();
//--------------函数部分
	CLaneTel();
	virtual ~CLaneTel() {};
	
	//主要的处理函数
	bool InitSystem ();	//装载系统	
	void ExitSystem ();	//卸载系统
	void TelProc ();	//电话的过程
	
	//外部调用的辅助性函数
	int  GetChannelsNum ();
	void GetLineState ( ChannelStruct *pChanStruct, WORD wChannelNo );

protected:
	
	//内部调用的辅助性函数
	void GetVoicePath ();
	void GetRecordPath ();

//--------------变量部分-----
protected:
	char m_sRecFaxPath[100];
	void GetRecFaxPath();

	int			m_iTotalLine;		//本卡的的线路的总数
	char		m_sVoicePath[100];	//Voice所在目录
	char		m_sRecordPath[100];	//Record所在的目录
	
	CChannel	* m_pChannels[16];		//线路状态的数组
	int			m_iOutLineNo;			//使用的外线通道号
	int			m_iUseInLineNum;		//使用的内线通道数量
	int			m_iUseLineNum;			//使用的通道的数量
	
	bool		m_bUseFax;				//是否使用传真
	int			m_iFaxLineNo;			//传真要用的通道号
	COutChannelWithFax	* m_pFaxChannel;	//传真通道对象的指针
};

#endif	//LANE_TEL_H
