//////////////////////////////////////////////////////////////////////////////////////////////////
//
// 文件: CreatGrammar.cpp
//
// 日期：2005年1月22日
//
// 作者: 吕宝虹 (C) All Rights Reserved
//
// 描述: 根据人名和机器名生成语音识别引擎用的文法文件--*.xml
//
//////////////////////////////////////////////////////////////////////////////////////////////////

#include "SerFrame.h"
#include "stdafx.h"
#include "CreatGrammar.h"
#define _UNICONDE
#define UNICONDE

//保存文件名到成员变量
CGrammarFile::CGrammarFile( char *sFileName )
{
	strcpy( m_sGraFileName, sFileName );
	m_bEnableWrite = FALSE;
}

CGrammarFile::~CGrammarFile()
{

}

//写文法文件头和定义头
void CGrammarFile::WriteGraStart()
{
	FILE* pFile = NULL;
	pFile = fopen ( m_sGraFileName, "wb" );
	fclose ( pFile );
	pFile = fopen ( m_sGraFileName, "a+" );

	if ( pFile != NULL ) {

		fprintf ( pFile, "<?xml version=\"1.0\" encoding=\"GB2312\"?>\n" );
		//写文件头
		fprintf ( pFile, "<GRAMMAR LANGID=\"804\">\n" );
		//写定义头
		fprintf( pFile, "\t<DEFINE>\n");
		fclose ( pFile );

		m_bEnableWrite = TRUE;
	}
}

//写定义内容
void CGrammarFile::WriteDefine( int value )
{
	if ( m_bEnableWrite ) {
		FILE *pFile = NULL;
		pFile = fopen (  m_sGraFileName, "a+");
		if ( pFile != NULL ) {
			char buf[256];

			// 生成<ID NAME="VID_SubNamexxxx" VAL="xxxx">
			sprintf ( buf, "\t\t<ID NAME=\"VID_SubName%d\" VAL=\"%d\"/>\n", value, value+4000 );

			fprintf ( pFile, buf );
			fclose ( pFile );
		}
	}
}

//写定义结尾，写顶级规则，人名规则头
void CGrammarFile::WriteTopRule()
{
	if ( m_bEnableWrite ) {
		FILE *pFile = NULL;
		pFile = fopen (  m_sGraFileName, "a+");
		if ( pFile != NULL ) {

			//写定义结尾
			fprintf(pFile, "\t\t<ID NAME=\"VID_SubNameRule\" VAL=\"3001\"/>\n");
			fprintf(pFile, "\t\t<ID NAME=\"VID_TopLevelRule\" VAL=\"3000\"/>\n");
			fprintf(pFile, "\t</DEFINE>\n");

			//写顶级规则
			fprintf ( pFile, "\t<RULE ID=\"VID_TopLevelRule\" TOPLEVEL=\"ACTIVE\">\n");

			fprintf ( pFile, "\t\t<O>\n\t\t\t<L>\n");	//<O>????????????????

			fprintf ( pFile, "\t\t\t\t<P>我</P>\n");
			fprintf ( pFile, "\t\t\t\t<P>要</P>\n");
			fprintf ( pFile, "\t\t\t\t<P>请</P>\n");
			fprintf ( pFile, "\t\t\t\t<P>叫</P>\n");
			fprintf ( pFile, "\t\t\t\t<P>找</P>\n");
			fprintf ( pFile, "\t\t\t\t<P>一</P>\n");
			fprintf ( pFile, "\t\t\t\t<P>下</P>\n");

			fprintf ( pFile, "\t\t\t</L>\n\t\t</O>\n");	//<O>??????????????

			fprintf ( pFile, "\t\t<RULEREF REFID=\"VID_SubNameRule\" />\n");

			fprintf ( pFile, "\t</RULE>\n");

			//写名字规则头
			fprintf ( pFile, "\t<RULE ID=\"VID_SubNameRule\" >\n");
			fprintf ( pFile, "\t\t<L PROPID=\"VID_SubNameRule\">\n");

			fclose ( pFile );
		}
	}
}

//写名字规则体
void CGrammarFile::WriteNameRule( int value , char *name )
{
	if ( m_bEnableWrite ) {
		FILE *pFile = NULL;
		pFile = fopen (  m_sGraFileName, "a+");
		if ( pFile != NULL ) {
			char buf[256];

			// 生成<ID NAME="VID_SubNamexxxx" VAL="xxxx">
			sprintf ( buf, "\t\t\t<P VAL=\"VID_SubName%d\">%s</P>\n", value, name )	;

			fprintf ( pFile, buf );
			fclose ( pFile );
		}
	}
}

//写名字规则尾，写文法文件结尾
void CGrammarFile::WriteGraEnd()
{
	if ( m_bEnableWrite ) {
		FILE *pFile = NULL;
		pFile = fopen(m_sGraFileName, "a+");

		if ( pFile != NULL ) {

			//写名字规则尾
			fprintf ( pFile, "\t\t</L>\n" );
			fprintf ( pFile, "\t</RULE>\n" );

			//写文法文件尾
			fprintf ( pFile, "</GRAMMAR>" );
			fclose  (pFile );
		}
		m_bEnableWrite = FALSE;
	}
}