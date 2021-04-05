#ifndef LANE_TEL_DEFINE_H
#define LANE_TEL_DEFINE_H

#define 	EMPTY_CHANNEL_NO		1024

#define		CHTYPE_TRUNK_WITH_FAX	10	//带传真功能的通道类型

#define		OutReturn_Nothing		0	//没有需要返回的
#define		OutReturn_LinkInLine	1	//要连接内线
#define		OutReturn_HangUp		3	//外线已经挂机

#define		InReturn_Nothing		7	//没有需要返回的
#define		InReturn_NoListen		8	//内线无人接听
#define		InReturn_FeedOffHook	9	//内线已经摘机，准备连通
#define		InReturn_HangUp			10	//内线已经挂机

#define		FaxReturn_Nothing		14	//没有需要返回的
#define		FaxReturn_NoFreeFaxCh	15	//没有空闲传真通道
#define		FaxReturn_LinkFail		16	//连接失败
#define		FaxReturn_SendFail		17	//发送失败
#define		FaxReturn_SendSuccess	18	//发送成功


enum CHANNEL_STATE {
//-------------------外线通道的状态---------------------
	CH_FREE,			//空闲 状态
	CH_OFFHOOK,			//摘机 状态
	CH_WELCOME,			//播送欢迎信息 状态
	CH_SELECT,			//主菜单选择 状态
	
	CH_RECORD_MESSAGE_START,		//留言开始 状态
	CH_RECORD_MESSAGE_ING,			//正在留言 状态
	CH_RECORD_MESSAGE_END,			//留言结束 状态
	
	CH_CALL_BY_SPEECH_START,		//语音识别找人开始 状态
	CH_CALL_BY_SPEECH_RECORDING,	//语音识别找人正在录音 状态
	CH_CALL_BY_SPEECH_RECONITION,	//语音识别找人正在识别 状态
	
	CH_CALL_BY_DTMF_START,			//按键找人开始 状态
	CH_CALL_BY_DTMF_GETDTMF,		//获得按键码 状态
	CH_CALL_BY_DTMF_SEARCHING,		//根据按键码搜索数据库 状态
	
	//CH_WAIT_LINK,					//等待与内线相连
	CH_INLINE_BUSY,					//处理内线忙 状态
	CH_INLINE_HANGUP,				//处理通话中内线挂机 状态
	CH_TALKING_WITH_IN,				//正在与内线通话中 状态
	
//-------------------内线通道的状态---------------------
	//CH_FREE,				//空闲 状态
	//CH_OFFHOOK,			//摘机 状态
	CH_CHOICE_MESSAGE,		//选择要播放的留言 状态
	CH_PLAY_MESSAGE_START,	//开始播放留言 状态
	CH_PLAY_MESSAGE_ING,	//正在播放留言 状态
	CH_PLAY_MESSAGE_END,	//结束播放留言 状态
	
	CH_RINGING,				//给内线振铃 状态
	CH_WAIT_OFFHOOK,		//等待内线摘机 状态
	CH_NO_LISTEN,			//内线无人接听 状态
	
	CH_FEED_OFFHOOK,		//要与外线连通情况下的内线摘机 状态
	CH_WAIT_LINK,			//等待与外线连通 状态
	
	CH_TALKING_WITH_OUT,	//正在与外线通话 状态
	CH_OUT_HANGUP,			//外线已经挂机 状态
	CH_WAIT_IN_HANGUP,		//（外线已挂机）等待内线挂机 状态
		
//-------------------悬空通道的状态---------------------
	CH_EMPTY,				//悬空 状态

//-------------------传真通道状态-----------------------
	//CH_FREE,				//空闲 状态
	//CH_OFFHOOK,			//摘机 状态
	//CH_WELCOME,			//播送欢迎信息 状态
	//CH_SELECT,			//主菜单选择 状态
	CH_RECEIVE_FAX_LINK,	//在为接收传真建立连接
	CH_RECEIVE_FAX_START,	//开始接收传真
	CH_RECEIVE_FAX_ING,		//正在接收传真
	CH_RECEIVE_FAX_END,		//接收传真结束
	
	CH_SEND_FAX_LINK,		//在为发送传真建立连接
	CH_SEND_FAX_DAIL,		//正在拨号
	CH_SEND_FAX_START,		//开始发送传真
	CH_SEND_FAX_ING,		//正在发送传真
	CH_SEND_FAX_END			//传真发送结束
};

//用于向界面显示
struct ChannelStruct {
	WORD	wChannelNo;					//通道号
	int		iType;						//通道类型
	int     iState;						//通道状态
	char	sCallerID[32];				//来电ID
	char	sNowRecordFileName[128];	//当前录音的文件名
};

//用于向外界显示的传真方面的信息
struct FaxChnlStruct {
	WORD	wChannelNo;
	int		iType;
	int		iState;
	char	sCallerID[32];				//来电ID
	char	sNowRecFaxName[128];
};

//从OutLine中获得的连接方面的信息
struct LinkInfo {
	WORD		wInLineNo;	//外线要连接的内线通道号
	CString		sHostName;	//要发消息提醒的主机名
	CString		sCallerID;	//来电电话号码
};


#endif	// LANE_TEL_DEFINE_H