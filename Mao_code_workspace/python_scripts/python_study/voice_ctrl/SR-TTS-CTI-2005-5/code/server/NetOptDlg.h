#if !defined(AFX_NETOPTDLG_H__20B05F50_46D1_476B_B9E7_5239E674964F__INCLUDED_)
#define AFX_NETOPTDLG_H__20B05F50_46D1_476B_B9E7_5239E674964F__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000
// NetOptDlg.h : header file
//

/////////////////////////////////////////////////////////////////////////////
// CNetOptDlg dialog

class CNetOptDlg : public CDialog
{
// Construction
public:
	CNetOptDlg(CWnd* pParent = NULL);   // standard constructor

// Dialog Data
	//{{AFX_DATA(CNetOptDlg)
	enum { IDD = IDD_NETOPT };
	CString	m_sServerIP;
	int		m_iPort;
	//}}AFX_DATA


// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CNetOptDlg)
	public:
	virtual BOOL PreTranslateMessage(MSG* pMsg);
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:

	// Generated message map functions
	//{{AFX_MSG(CNetOptDlg)
	afx_msg void On_Ok();
	afx_msg void On_Cancel();
	virtual BOOL OnInitDialog();
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_NETOPTDLG_H__20B05F50_46D1_476B_B9E7_5239E674964F__INCLUDED_)
