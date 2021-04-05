//////////////////////////////////////////////////////////////////////////////////////////////////
//
// 文件: SerFrameDlg.h
//
// 日期：2005年1月21日
//
// 作者: 吕宝虹 (C) All Rights Reserved
//
// 描述: 程序的主界面
//
//////////////////////////////////////////////////////////////////////////////////////////////////
#if !defined(AFX_SERFRAMEDLG_H__772B5B8D_5813_49B3_B3CE_6B4C15472815__INCLUDED_)
#define AFX_SERFRAMEDLG_H__772B5B8D_5813_49B3_B3CE_6B4C15472815__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

class CSerFrameDlgAutoProxy;

#include "namelist.h"
#include "LaneTel.h"

/////////////////////////////////////////////////////////////////////////////
// CSerFrameDlg dialog

class CSerFrameDlg : public CDialog
{
	DECLARE_DYNAMIC(CSerFrameDlg);
	friend class CSerFrameDlgAutoProxy;

protected:
	bool m_bTelRun;			//电话系统运行标记
	CLaneTel m_Tel;			//电话系统的对象
	void ShowTelState();	//显示电话系统运行的状态
	int m_nTimer;			//计时器

public:
	void ShowFaxState();
	CSerFrameDlg(CWnd* pParent = NULL);	// standard constructor
	virtual ~CSerFrameDlg();

// Dialog Data
	//{{AFX_DATA(CSerFrameDlg)
	enum { IDD = IDD_SERFRAME_DIALOG };
	CListCtrl	m_FaxReport;
	CListCtrl	m_TelReport;
	CString	m_szFaxDialNo;
	//}}AFX_DATA

	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CSerFrameDlg)
	public:
	virtual BOOL PreTranslateMessage(MSG* pMsg);
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:
	CSerFrameDlgAutoProxy* m_pAutoProxy;
	HICON m_hIcon;
	BOOL CanExit();

	// Generated message map functions
	//{{AFX_MSG(CSerFrameDlg)
	virtual BOOL OnInitDialog();
	afx_msg void OnSysCommand(UINT nID, LPARAM lParam);
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	afx_msg void OnManageName();
	afx_msg void OnClose();
	afx_msg void OnFaxopt();
	afx_msg void OnStart();
	afx_msg void OnStop();
	afx_msg void OnTimer(UINT nIDEvent);
	afx_msg void OnDestroy();
	afx_msg void OnTelOpt();
	afx_msg void OnNetOpt();
	afx_msg void OnSendFax();
	afx_msg void OnTest();
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
private:
	void NetInit();
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_SERFRAMEDLG_H__772B5B8D_5813_49B3_B3CE_6B4C15472815__INCLUDED_)
