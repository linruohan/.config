//////////////////////////////////////////////////////////////////////////////////////////////////
//
// 文件: CLog.h
//
// 作者: 吕宝虹 (C) All Rights Reserved---修改自Andy Pike的directx 8.0教程
//
// 描述: 记录日志到.htm文件
//
//////////////////////////////////////////////////////////////////////////////////////////////////

#ifndef __CLogH__
#define __CLogH__

#include <stdio.h>
#include <stdarg.h>
#include <windows.h>


class CLog
{
private:
	
	BOOL	m_bEnableLogging;
	char	m_sLogFileName[24];
public:
	void LogTopic( char *lpszText, ... );
	CLog( char *sFileName );
	virtual ~CLog();

	void StartLogging();
	void StopLogging();
	void LogError(char *lpszText, ...);
	void LogInfo(char *lpszText, ...);
	void LogWarning(char *lpszText, ...);

};

#endif // __CLogH__
