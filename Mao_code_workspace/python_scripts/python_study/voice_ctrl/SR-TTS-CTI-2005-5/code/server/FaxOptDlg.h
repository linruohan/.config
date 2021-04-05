#if !defined(AFX_FAXOPTDLG_H__802A8D43_9D65_4715_91B1_8A3B4279D24E__INCLUDED_)
#define AFX_FAXOPTDLG_H__802A8D43_9D65_4715_91B1_8A3B4279D24E__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000
// FaxOptDlg.h : header file
//

/////////////////////////////////////////////////////////////////////////////
// CFaxOptDlg dialog

class CFaxOptDlg : public CDialog
{
// Construction
public:
	CFaxOptDlg(CWnd* pParent = NULL);   // standard constructor

// Dialog Data
	//{{AFX_DATA(CFaxOptDlg)
	enum { IDD = IDD_FAXOPT };
	int		m_iOutLineNoWithFax;
	//}}AFX_DATA


// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CFaxOptDlg)
	public:
	virtual BOOL PreTranslateMessage(MSG* pMsg);
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:

	// Generated message map functions
	//{{AFX_MSG(CFaxOptDlg)
	virtual BOOL OnInitDialog();
	afx_msg void On_Ok();
	afx_msg void On_Cancel();
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_FAXOPTDLG_H__802A8D43_9D65_4715_91B1_8A3B4279D24E__INCLUDED_)
