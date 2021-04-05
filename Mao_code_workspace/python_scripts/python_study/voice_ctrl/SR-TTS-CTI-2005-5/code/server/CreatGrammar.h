//////////////////////////////////////////////////////////////////////////////////////////////////
//
// 文件: CreatGrammar.h
//
// 日期：2005年1月22日
//
// 作者: 吕宝虹 (C) All Rights Reserved
//
// 描述: 根据人名和机器名生成语音识别引擎用的文法文件--*.xml
//
//////////////////////////////////////////////////////////////////////////////////////////////////

#ifndef LANE_CREATGRAMMAR_H
#define LANE_CREATGRAMMAR_H

#include <stdio.h>
#include <stdarg.h>
#include <windows.h>

//#include <wchar.h>

class CGrammarFile
{
private:

	BOOL	m_bEnableWrite;
	char	m_sGraFileName[24];


public:

	CGrammarFile( char *sFileName );
	virtual ~CGrammarFile();

	void WriteGraStart();		//调用次序1
	void WriteDefine( int value );
	void WriteTopRule();
	void WriteNameRule( int value , char *name );
	void WriteGraEnd();		//调用次序5

};
#endif // LANE_CREATGRAMMAR_H