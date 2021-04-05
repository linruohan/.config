#if !defined(AFX_SHOWALLCHANTYPEDLG_H__4BC60E8E_41E2_4657_961B_BEA1442EEA84__INCLUDED_)
#define AFX_SHOWALLCHANTYPEDLG_H__4BC60E8E_41E2_4657_961B_BEA1442EEA84__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000
// ShowAllChanTypeDlg.h : header file
//

/////////////////////////////////////////////////////////////////////////////
// CShowAllChanTypeDlg dialog

class CShowAllChanTypeDlg : public CDialog
{
// Construction
public:
	CShowAllChanTypeDlg(CWnd* pParent = NULL);   // standard constructor

// Dialog Data
	//{{AFX_DATA(CShowAllChanTypeDlg)
	enum { IDD = IDD_CHANNELTYPE };
	CListCtrl	m_ChannelList;
	//}}AFX_DATA


// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CShowAllChanTypeDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:

	// Generated message map functions
	//{{AFX_MSG(CShowAllChanTypeDlg)
	virtual BOOL OnInitDialog();
	afx_msg void OnDestroy();
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_SHOWALLCHANTYPEDLG_H__4BC60E8E_41E2_4657_961B_BEA1442EEA84__INCLUDED_)
