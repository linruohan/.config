#if !defined(AFX_TELOPT_H__EF4A98E2_55C6_42DB_AE8A_F3E5B275994B__INCLUDED_)
#define AFX_TELOPT_H__EF4A98E2_55C6_42DB_AE8A_F3E5B275994B__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000
// TelOpt.h : header file
//

#include "CIniFile.h"	//iniÎÄ¼þ²Ù×÷

/////////////////////////////////////////////////////////////////////////////
// CTelOptDlg dialog

class CTelOptDlg : public CDialog
{
// Construction
public:
	CTelOptDlg(CWnd* pParent = NULL);   // standard constructor

// Dialog Data
	//{{AFX_DATA(CTelOptDlg)
	enum { IDD = IDD_TELOPT };
	int		m_iInLineNum;
	int		m_iInLine1;
	int		m_iInLine2;
	int		m_iInLine3;
	int		m_iInLine4;
	int		m_iInLine5;
	int		m_iInLine6;
	int		m_iOutLineNo;
	//}}AFX_DATA


// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CTelOptDlg)
	public:
	virtual BOOL PreTranslateMessage(MSG* pMsg);
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:

	// Generated message map functions
	//{{AFX_MSG(CTelOptDlg)
	afx_msg void On_Cancel();
	afx_msg void On_Ok();
	virtual BOOL OnInitDialog();
	afx_msg void OnShowAllChannel();
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_TELOPT_H__EF4A98E2_55C6_42DB_AE8A_F3E5B275994B__INCLUDED_)
