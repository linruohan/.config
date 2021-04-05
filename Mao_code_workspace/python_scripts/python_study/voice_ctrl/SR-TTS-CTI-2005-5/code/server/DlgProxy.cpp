// DlgProxy.cpp : implementation file
//

#include "stdafx.h"
#include "SerFrame.h"
#include "DlgProxy.h"
#include "SerFrameDlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CSerFrameDlgAutoProxy

IMPLEMENT_DYNCREATE(CSerFrameDlgAutoProxy, CCmdTarget)

CSerFrameDlgAutoProxy::CSerFrameDlgAutoProxy()
{
	EnableAutomation();
	
	// To keep the application running as long as an automation 
	//	object is active, the constructor calls AfxOleLockApp.
	AfxOleLockApp();

	// Get access to the dialog through the application's
	//  main window pointer.  Set the proxy's internal pointer
	//  to point to the dialog, and set the dialog's back pointer to
	//  this proxy.
	ASSERT (AfxGetApp()->m_pMainWnd != NULL);
	ASSERT_VALID (AfxGetApp()->m_pMainWnd);
	ASSERT_KINDOF(CSerFrameDlg, AfxGetApp()->m_pMainWnd);
	m_pDialog = (CSerFrameDlg*) AfxGetApp()->m_pMainWnd;
	m_pDialog->m_pAutoProxy = this;
}

CSerFrameDlgAutoProxy::~CSerFrameDlgAutoProxy()
{
	// To terminate the application when all objects created with
	// 	with automation, the destructor calls AfxOleUnlockApp.
	//  Among other things, this will destroy the main dialog
	if (m_pDialog != NULL)
		m_pDialog->m_pAutoProxy = NULL;
	AfxOleUnlockApp();
}

void CSerFrameDlgAutoProxy::OnFinalRelease()
{
	// When the last reference for an automation object is released
	// OnFinalRelease is called.  The base class will automatically
	// deletes the object.  Add additional cleanup required for your
	// object before calling the base class.

	CCmdTarget::OnFinalRelease();
}

BEGIN_MESSAGE_MAP(CSerFrameDlgAutoProxy, CCmdTarget)
	//{{AFX_MSG_MAP(CSerFrameDlgAutoProxy)
		// NOTE - the ClassWizard will add and remove mapping macros here.
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

BEGIN_DISPATCH_MAP(CSerFrameDlgAutoProxy, CCmdTarget)
	//{{AFX_DISPATCH_MAP(CSerFrameDlgAutoProxy)
		// NOTE - the ClassWizard will add and remove mapping macros here.
	//}}AFX_DISPATCH_MAP
END_DISPATCH_MAP()

// Note: we add support for IID_ISerFrame to support typesafe binding
//  from VBA.  This IID must match the GUID that is attached to the 
//  dispinterface in the .ODL file.

// {B0EFB0E7-940A-420E-8BDA-1B692BB01BEC}
static const IID IID_ISerFrame =
{ 0xb0efb0e7, 0x940a, 0x420e, { 0x8b, 0xda, 0x1b, 0x69, 0x2b, 0xb0, 0x1b, 0xec } };

BEGIN_INTERFACE_MAP(CSerFrameDlgAutoProxy, CCmdTarget)
	INTERFACE_PART(CSerFrameDlgAutoProxy, IID_ISerFrame, Dispatch)
END_INTERFACE_MAP()

// The IMPLEMENT_OLECREATE2 macro is defined in StdAfx.h of this project
// {03E77512-2203-4512-8033-542695039192}
IMPLEMENT_OLECREATE2(CSerFrameDlgAutoProxy, "SerFrame.Application", 0x3e77512, 0x2203, 0x4512, 0x80, 0x33, 0x54, 0x26, 0x95, 0x3, 0x91, 0x92)

/////////////////////////////////////////////////////////////////////////////
// CSerFrameDlgAutoProxy message handlers
