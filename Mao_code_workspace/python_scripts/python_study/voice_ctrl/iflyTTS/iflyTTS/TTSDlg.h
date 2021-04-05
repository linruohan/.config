// TTSDlg.h : header file
//

#pragma once
#include <string>
#include <list>
#include <vector>
#include <sstream>
#include <fstream>
#include "iFlySTTSApi.h"
using namespace std;
//#include <atlbase.h>		// ATL
//#include <sapi.h>           // SAPI includes
//#include <sphelper.h>
//#include <spuihelp.h>
//#include "Page.h"

// CTTSDlg dialog
class CTTSDlg : public CDialog
{
// Construction
public:
	CTTSDlg(CWnd* pParent = NULL);	// standard constructor
	~CTTSDlg();
// Dialog Data
	enum { IDD = IDD_TTS_DIALOG };

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support


// Implementation
protected:
	HICON m_hIcon;
	HRESULT hr;
	// Generated message map functions
	virtual BOOL OnInitDialog();
	 void OnPaint();
	 HCURSOR OnQueryDragIcon();
	DECLARE_MESSAGE_MAP()
private:
	list<string> m_page;
	list<string>::iterator m_senPos;
	int m_speed;
	int m_timer;
	bool m_isStop;
	bool m_isPause;
	bool m_isInit;
	bool m_isStart;
	HTTSINSTANCE m_hTTSInstance;
public:
	void LoadPage(const string filename);	
public:
	HRESULT InitSapi();
	void ReleaseSapi();
	afx_msg void OnPlay();
	 void OnPause();
	 void OnStop();
	 void OnIncreaseRate();
	 void OnDecreaseRate();
	 LRESULT OnEndSpeak(WPARAM wParam, LPARAM lPARAM);
public:
	virtual BOOL PreTranslateMessage(MSG* pMsg);
protected:
	virtual void OnCancel();
	virtual void OnOK();
public:
	afx_msg void OnTimer(UINT_PTR nIDEvent);
private:
	vector<string> m_bookIndex;
	
	int m_readTag[1000];	//阅读标记
	int m_saveTag[1000];	//录制标记

	int m_lastReadBook;		//阅读书标记
	int m_lastSaveBook;		//录制书标记

	int m_currentBook;
	int m_currentPage;

	bool m_isLoad;

	bool m_isSave;
	bool m_isCover;

	bool m_isDelete;
	bool m_isDelBook;

	int m_curSaveBook;
	int m_curSavePage;
	
public:
	void InitIndex();
	void SaveIndex();

	void NextBook();
	void PreBook();

	void NextPage();
	void PrePage();

	void CheckSavePage();
	void SavePage();
	void LoadSavedPage();

	void CheckDelete();
	void Delete();
};
