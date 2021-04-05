//////////////////////////////////////////////////////////////////////////////////////////////////
//
// 文件: CLog.cpp
//
// 作者: 吕宝虹 (C) All Rights Reserved---修改自Andy Pike的directx 8.0教程
//
// 描述: 记录日志到.htm文件,首先要执行StartLogging()，然后执行LogTopic()、
//		 LogError()、LogInfo()、LogWarning()等，最后结束纪录要执行StartLogging()
//
//////////////////////////////////////////////////////////////////////////////////////////////////
#include "stdafx.h"
#include "CLog.h"

CLog::CLog( char *sFileName )
{
	strcpy( m_sLogFileName, sFileName );
	m_bEnableLogging = FALSE;
}

CLog::~CLog()
{

}

void CLog::LogError(char *lpszText, ...)
{
	if(m_bEnableLogging)
	{
		va_list argList;
		FILE *pFile = NULL;

		//Initialize variable argument list
		va_start(argList, lpszText);

		//Open the log file for appending
		pFile = fopen(m_sLogFileName, "a+");

		if(pFile != NULL)
		{
			//Write the error to the log file
			fprintf(pFile, "<font face=\"Arial\" size=\"2\" color=\"#FF0000\"><b><li>错误:&nbsp;&nbsp;");
			vfprintf(pFile, lpszText, argList);
			fprintf(pFile, "</b></font><br>\n");

			//Close the file
			fclose(pFile);
		}

		va_end(argList);
	}
}

void CLog::LogInfo(char *lpszText, ...)
{
	if(m_bEnableLogging)
	{
		va_list argList;
		FILE *pFile = NULL;

		//Initialize variable argument list
		va_start(argList, lpszText);

		//Open the log file for appending
		pFile = fopen(m_sLogFileName, "a+");

		if(pFile != NULL)
		{
			//Write the error to the log file
			fprintf(pFile, "<font face=\"Arial\" size=\"2\" color=\"#000000\"><b><li>信息:&nbsp;&nbsp;");
			vfprintf(pFile, lpszText, argList);
			fprintf(pFile, "<b></font><br>\n");

			//Close the file
			fclose(pFile);
		}

		va_end(argList);
	}
}

void CLog::LogWarning(char *lpszText, ...)
{
	if(m_bEnableLogging)
	{
		va_list argList;
		FILE *pFile = NULL;

		//Initialize variable argument list
		va_start(argList, lpszText);

		//Open the log file for appending
		pFile = fopen(m_sLogFileName, "a+");

		if(pFile != NULL)
		{
			//Write the error to the log file
			fprintf(pFile, "<font face=\"Arial\" size=\"2\" color=\"#E7651A\"><b><li>警告:&nbsp;&nbsp;");
			vfprintf(pFile, lpszText, argList);
			fprintf(pFile, "</b></font><br>\n");

			//Close the file
			fclose(pFile);
		}

		va_end(argList);
	}
}

void CLog::StartLogging()
{
	FILE* pFile = NULL;

	//OPen the file and clear the contents
	pFile = fopen(m_sLogFileName, "wb");

	if(pFile != NULL)
	{
		//Write start html to log
		fprintf(pFile, "<html><head><title>Log File</title></head><body>\n");
		fprintf(pFile, "<font face=\"Arial\" size=\"5\" color=\"#000000\"><b>Log File</b></font><br><hr color=#000000>\n");

		//Close the file
		fclose(pFile);

		m_bEnableLogging = TRUE;
	}
}

void CLog::StopLogging()
{
	if(m_bEnableLogging)
	{
		FILE *pFile = NULL;

		//Open the log file for appending
		pFile = fopen(m_sLogFileName, "a+");

		if(pFile != NULL)
		{
			//Write end html to log
			fprintf(pFile, "</body></html>");

			//Close the file
			fclose(pFile);
		}

		m_bEnableLogging = FALSE;
	}
}

void CLog::LogTopic(char *lpszText, ...)
{
	if(m_bEnableLogging)
	{
		va_list argList;
		FILE *pFile = NULL;

		//Initialize variable argument list
		va_start(argList, lpszText);

		//Open the log file for appending
		pFile = fopen(m_sLogFileName, "a+");

		if(pFile != NULL)
		{
			//Write the error to the log file
			fprintf(pFile, "<br><font face=\"Arial\" size=\"3\" color=\"#0066FF\"><b>");
			vfprintf(pFile, lpszText, argList);
			fprintf(pFile, "</b></font><br>\n");

			//Close the file
			fclose(pFile);
		}

		va_end(argList);
	}
}
