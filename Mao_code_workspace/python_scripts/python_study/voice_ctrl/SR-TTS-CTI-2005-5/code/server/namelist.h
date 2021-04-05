//////////////////////////////////////////////////////////////////////////////////////////////////
//
// 文件: namelist.h
//
// 日期：2005年1月22日
//
// 作者: 吕宝虹 (C) All Rights Reserved
//
// 描述: 连接数据源，对数据库中的人员姓名和主机进行各种操作，并生成文法文件*.xml。要使用CNameListBind
//
//////////////////////////////////////////////////////////////////////////////////////////////////

#if !defined(AFX_NAMELIST_H__972352B5_7BD0_4533_A707_DFA6B44B010E__INCLUDED_)
#define AFX_NAMELIST_H__972352B5_7BD0_4533_A707_DFA6B44B010E__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000
// namelist.h : header file
//
/////////////////////////////////////////////////////////////////////////////
// CNameList dialog

class CNameList : public CDialog
{
public:
	int GetInLineNoByHost ( CString sHostName );
	long GetHostByDtmf(CString sDtmfNo, char pstrHost[][128], int iHostCount );
	long GetHostByName ( CString sPersonName, char pstrHost[][128], int iHostCount );
	
	CNameList ( CWnd* pParent = NULL ); //连接数据库
	virtual ~CNameList ();				//关闭数据库

protected:
	void SetupConnect ();			//建立数据库连接
	BOOL CheckInputValidity();		//检查输入数据的合法性
	BOOL CheckInputIntegrality();	//检查输入数据的完整性
	void ShowAll();					//列出数据库里所有的记录
	
	CString m_sOldHostName;	//当选中列表一个条目时，保存旧的主机名，以便在OnPersonEdit()中用
	_ConnectionPtr m_DBCnt;	//数据库连接接口

// Dialog Data
	//{{AFX_DATA(CNameList)
	enum { IDD = IDD_NAMELIST };
	CListCtrl	m_NameList;
	CString	m_sHostName;
	CString	m_sPersonName;
	CString	m_sDtmfNo;
	CString	m_sInLineNo;
	//}}AFX_DATA

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CNameList)
	public:
	virtual void OnFinalRelease();
	virtual BOOL PreTranslateMessage(MSG* pMsg);
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:
	// Generated message map functions
	//{{AFX_MSG(CNameList)
	virtual BOOL OnInitDialog();
	afx_msg void OnClose();
	afx_msg void OnDestroy();
	afx_msg void OnClickNamelist(NMHDR* pNMHDR, LRESULT* pResult);
	afx_msg void OnPersonNew();
	afx_msg void OnPersonDel();
	afx_msg void OnPersonEdit();
	afx_msg void OnPersonSearch();
	afx_msg void OnShowAll();
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
	// Generated OLE dispatch map functions
	//{{AFX_DISPATCH(CNameList)
		// NOTE - the ClassWizard will add and remove member functions here.
	//}}AFX_DISPATCH
	DECLARE_DISPATCH_MAP()
	DECLARE_INTERFACE_MAP()
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_NAMELIST_H__972352B5_7BD0_4533_A707_DFA6B44B010E__INCLUDED_)
