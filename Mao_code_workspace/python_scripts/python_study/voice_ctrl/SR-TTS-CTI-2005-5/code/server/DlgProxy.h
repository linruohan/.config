// DlgProxy.h : header file
//

#if !defined(AFX_DLGPROXY_H__C6CC8E8E_B07A_4001_9072_E8E1C809FFE6__INCLUDED_)
#define AFX_DLGPROXY_H__C6CC8E8E_B07A_4001_9072_E8E1C809FFE6__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

class CSerFrameDlg;

/////////////////////////////////////////////////////////////////////////////
// CSerFrameDlgAutoProxy command target

class CSerFrameDlgAutoProxy : public CCmdTarget
{
	DECLARE_DYNCREATE(CSerFrameDlgAutoProxy)

	CSerFrameDlgAutoProxy();           // protected constructor used by dynamic creation

// Attributes
public:
	CSerFrameDlg* m_pDialog;

// Operations
public:

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CSerFrameDlgAutoProxy)
	public:
	virtual void OnFinalRelease();
	//}}AFX_VIRTUAL

// Implementation
protected:
	virtual ~CSerFrameDlgAutoProxy();

	// Generated message map functions
	//{{AFX_MSG(CSerFrameDlgAutoProxy)
		// NOTE - the ClassWizard will add and remove member functions here.
	//}}AFX_MSG

	DECLARE_MESSAGE_MAP()
	DECLARE_OLECREATE(CSerFrameDlgAutoProxy)

	// Generated OLE dispatch map functions
	//{{AFX_DISPATCH(CSerFrameDlgAutoProxy)
		// NOTE - the ClassWizard will add and remove member functions here.
	//}}AFX_DISPATCH
	DECLARE_DISPATCH_MAP()
	DECLARE_INTERFACE_MAP()
};

/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_DLGPROXY_H__C6CC8E8E_B07A_4001_9072_E8E1C809FFE6__INCLUDED_)
