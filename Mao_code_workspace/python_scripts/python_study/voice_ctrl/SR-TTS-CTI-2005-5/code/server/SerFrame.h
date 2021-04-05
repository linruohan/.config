//////////////////////////////////////////////////////////////////////////////////////////////////
//
// 文件: SerFrame.h			??????????????????
//
// 日期：2005年1月21日
//
// 作者: 吕宝虹 (C) All Rights Reserved
//
// 描述: 建立数据源
//
//////////////////////////////////////////////////////////////////////////////////////////////////

//需要建立数据源！！！？？？？？？？？？？？？？？？

#if !defined(AFX_SERFRAME_H__1A99E66B_3274_4D10_BE1B_3B98D7CB93D3__INCLUDED_)
#define AFX_SERFRAME_H__1A99E66B_3274_4D10_BE1B_3B98D7CB93D3__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"		// main symbols

//*绑定数据源
#include "odbcinst.h"//
#pragma  comment (lib,"Odbccp32")
//*/


/////////////////////////////////////////////////////////////////////////////
// CSerFrameApp:
// See SerFrame.cpp for the implementation of this class
//

class CSerFrameApp : public CWinApp
{
public:
	CSerFrameApp();

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CSerFrameApp)
	public:
	virtual BOOL InitInstance();
	virtual int ExitInstance();
	//}}AFX_VIRTUAL

// Implementation

	//{{AFX_MSG(CSerFrameApp)
		// NOTE - the ClassWizard will add and remove member functions here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_SERFRAME_H__1A99E66B_3274_4D10_BE1B_3B98D7CB93D3__INCLUDED_)
