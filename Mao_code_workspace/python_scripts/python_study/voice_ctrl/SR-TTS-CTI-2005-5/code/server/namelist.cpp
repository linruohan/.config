//////////////////////////////////////////////////////////////////////////////////////////////////
//
// 文件: namelist.cpp
//
// 日期：2005年1月22日
//
// 作者: 吕宝虹 (C) All Rights Reserved
//
// 描述: 连接数据源，对数据库中的人员姓名和主机进行各种操作，并生成文法文件*.xml。要使用CNameListBind
//
//////////////////////////////////////////////////////////////////////////////////////////////////
#include "stdafx.h"
#include "SerFrame.h"
#include "namelist.h"
#include "CreatGrammar.h"
//#include <locale.h>//在本地使用宽字符

#include "NameListBind.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CNameList dialog

CNameList::CNameList(CWnd* pParent /*=NULL*/)
	: CDialog(CNameList::IDD, pParent)
{
	EnableAutomation();
	//{{AFX_DATA_INIT(CNameList)
	m_sHostName = _T("");
	m_sPersonName = _T("");
	m_sDtmfNo = _T("");
	m_sInLineNo = _T("");
	//}}AFX_DATA_INIT

	m_DBCnt = NULL;
	SetupConnect();//连接数据库
}

// 关闭数据库
CNameList::~CNameList () 
{
	if ( m_DBCnt ) {
		m_DBCnt->Close();
		m_DBCnt = NULL;
	} 
}

void CNameList::OnFinalRelease()
{
	// When the last reference for an automation object is released
	// OnFinalRelease is called.  The base class will automatically
	// deletes the object.  Add additional cleanup required for your
	// object before calling the base class.
	CDialog::OnFinalRelease();
}

void CNameList::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CNameList)
	DDX_Control(pDX, IDC_NAMELIST, m_NameList);
	DDX_Text(pDX, IDE_HOSTNAME, m_sHostName);
	DDX_Text(pDX, IDE_PERSONNAME, m_sPersonName);
	DDX_Text(pDX, IDE_DTMFNO, m_sDtmfNo);
	DDX_Text(pDX, IDE_INLINENO, m_sInLineNo);
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CNameList, CDialog)
	//{{AFX_MSG_MAP(CNameList)
	ON_BN_CLICKED(IDB_CLOSE, OnClose)
	ON_WM_DESTROY()
	ON_NOTIFY(NM_CLICK, IDC_NAMELIST, OnClickNamelist)
	ON_BN_CLICKED(IDB_PERSONNEW, OnPersonNew)
	ON_BN_CLICKED(IDB_PERSONDEL, OnPersonDel)
	ON_BN_CLICKED(IDB_PERSONEDIT, OnPersonEdit)
	ON_BN_CLICKED(IDB_PERSONSEARCH, OnPersonSearch)
	ON_BN_CLICKED(IDB_SHOWALL, OnShowAll)
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

BEGIN_DISPATCH_MAP(CNameList, CDialog)
	//{{AFX_DISPATCH_MAP(CNameList)
		// NOTE - the ClassWizard will add and remove mapping macros here.
	//}}AFX_DISPATCH_MAP
END_DISPATCH_MAP()

// Note: we add support for IID_INameList to support typesafe binding
//  from VBA.  This IID must match the GUID that is attached to the
//  dispinterface in the .ODL file.

// {EB701AC9-800A-4C90-9B2C-B1F68A27FB53}
static const IID IID_INameList =
{ 0xeb701ac9, 0x800a, 0x4c90, { 0x9b, 0x2c, 0xb1, 0xf6, 0x8a, 0x27, 0xfb, 0x53 } };

BEGIN_INTERFACE_MAP(CNameList, CDialog)
	INTERFACE_PART(CNameList, IID_INameList, Dispatch)
END_INTERFACE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CNameList message handlers
void CNameList::OnDestroy()
{
	CDialog::OnDestroy();
}

//当列表中的一项被选中时，把选中的值显示到编辑框中
void CNameList::OnClickNamelist(NMHDR* pNMHDR, LRESULT* pResult)
{
	int i = m_NameList.GetSelectionMark();

	m_sHostName = m_NameList.GetItemText(i,0);
	m_sOldHostName = m_sHostName;
	m_sPersonName = m_NameList.GetItemText(i,1);
	m_sDtmfNo = m_NameList.GetItemText(i,2);
	m_sInLineNo = m_NameList.GetItemText(i,3);

	UpdateData(FALSE);
	*pResult = 0;
}

//屏蔽本对话框对回车键和ESC键阿响应
BOOL CNameList::PreTranslateMessage(MSG* pMsg)
{
	if(WM_KEYDOWN  ==	pMsg->message) {
		int nKey = (int) pMsg->wParam;
		if( (nKey == VK_RETURN) || (nKey == VK_ESCAPE) )	//没有VK_ENTER
		return true;
	}

	return CDialog::PreTranslateMessage(pMsg);
}

BOOL CNameList::OnInitDialog()
{
	CDialog::OnInitDialog();

	m_NameList.InsertColumn( 0,"主机名称" );
	m_NameList.InsertColumn( 1,"人员姓名" );
	m_NameList.InsertColumn( 2,"按键号码" );
	m_NameList.InsertColumn( 3,"内线通道号" );

	RECT rect;
	m_NameList.GetWindowRect(&rect);
	int wid = rect.right - rect.left;
	m_NameList.SetColumnWidth(0,wid/4);
	m_NameList.SetColumnWidth(1,wid/4);
	m_NameList.SetColumnWidth(2,wid/4);
	m_NameList.SetColumnWidth(3,wid/4);

	m_NameList.SetExtendedStyle(LVS_EX_FULLROWSELECT|LVS_EX_GRIDLINES|LVS_EX_HEADERDRAGDROP);

	m_NameList.DeleteAllItems();
	m_NameList.SetRedraw(FALSE);
	ShowAll();
	m_NameList.SetRedraw(TRUE);

	return TRUE;  // return TRUE unless you set the focus to a control
	              // EXCEPTION: OCX Property Pages should return FALSE
}



//------------------外部调用函数++++++++++++++++++++++++++++++++++++++++++++++++++++++++

long CNameList::GetHostByDtmf(CString sDtmfNo, char pstrHost[][128], int iHostCount)
{
	_RecordsetPtr pRst = NULL;			//Recordset的智能指针
	IADORecordBinding   *picRs = NULL;  //VC++ Extensions 接口指针声明（VC++扩展接口）
	CNameListBind  NameBind;

	try {
		//定义SQL语句
		CString SQL;
		SQL.Format("SELECT * FROM NameList WHERE DtmfNo='%s'", sDtmfNo);

		_bstr_t strSQL = SQL;

		TESTHR(pRst.CreateInstance(__uuidof(Recordset)));		//建立Recordset的接口
		pRst = m_DBCnt->Execute(strSQL, NULL, adCmdText);		//执行SQL语句

		//建立IADORecordBinding接口
		TESTHR(pRst->QueryInterface(__uuidof(IADORecordBinding),(LPVOID*)&picRs));
		TESTHR(picRs->BindToRecordset(&NameBind));		//绑定到CBook对象book

		int i = 0;

		while ( (!pRst->adoEOF) && (i<=iHostCount) )	//获得所有记录
		{
			strcpy ( pstrHost[i], NameBind.m_sz_HostName );
			i++;
			pRst->MoveNext();
		}
		picRs->Release();
		pRst->Close();
		return i;	//一共i条符合条件的记录
	}
	catch(_com_error& e) {	//异常处理
		AfxMessageBox(e.Description());
		return 0;
    }
}

//根据人员姓名得到主机名称列表，考虑到人员重名的情况下，就会有多台主机
long CNameList::GetHostByName(CString sPersonName, char pstrHost[10][128], int iHostCount )
{
	_RecordsetPtr pRst = NULL;			//Recordset的智能指针
	IADORecordBinding   *picRs = NULL;  //VC++ Extensions 接口指针声明（VC++扩展接口）
	CNameListBind  NameBind;

	try {
		//定义SQL语句
		CString SQL;
		SQL.Format("SELECT * FROM NameList WHERE PersonName='%s'", sPersonName);

		_bstr_t strSQL = SQL;

		TESTHR(pRst.CreateInstance(__uuidof(Recordset)));		//建立Recordset的接口
		pRst = m_DBCnt->Execute(strSQL, NULL, adCmdText);		//执行SQL语句

		//建立IADORecordBinding接口
		TESTHR(pRst->QueryInterface(__uuidof(IADORecordBinding),(LPVOID*)&picRs));
		TESTHR(picRs->BindToRecordset(&NameBind));		//绑定到CBook对象book

		int i = 0;

		while ( (!pRst->adoEOF) && (i<=iHostCount) )	//获得所有记录
		{
			strcpy ( pstrHost[i], NameBind.m_sz_HostName );
			i++;
			pRst->MoveNext();
		}
		picRs->Release();
		pRst->Close();
		return i;	//一共i条符合条件的记录
	}
	catch(_com_error& e) {	//异常处理
		AfxMessageBox(e.Description());
		return 0;
    }
}

int CNameList::GetInLineNoByHost(CString sHostName)
{
	_RecordsetPtr pRst = NULL;			//Recordset的智能指针
	IADORecordBinding   *picRs = NULL;  //VC++ Extensions 接口指针声明（VC++扩展接口）
	CNameListBind  NameBind;

	try {
		//定义SQL语句
		CString SQL;
		SQL.Format("SELECT * FROM NameList WHERE HostName='%s'", sHostName);

		_bstr_t strSQL = SQL;

		TESTHR(pRst.CreateInstance(__uuidof(Recordset)));		//建立Recordset的接口
		pRst = m_DBCnt->Execute(strSQL, NULL, adCmdText);		//执行SQL语句

		//建立IADORecordBinding接口
		TESTHR(pRst->QueryInterface(__uuidof(IADORecordBinding),(LPVOID*)&picRs));
		TESTHR(picRs->BindToRecordset(&NameBind));		//绑定到CBook对象book

		int i=0;
		char temp[8];
		while ( !pRst->adoEOF )	//获得所有记录
		{
			strcpy ( temp, NameBind.m_sz_InLineNo );
			i++ ;
			pRst->MoveNext();
		}
		if ( i == 0 ) {
			return 1024;
		}
		else {
			return  atoi ( temp );
		}
		picRs->Release();
		pRst->Close();
		return i;	//一共i条符合条件的记录
	}
	catch(_com_error& e) {	//异常处理
		AfxMessageBox(e.Description());
		return 1024;
    }
}


//-----------------人名管理操作辅助函数，类内部调用+++++++++++++++++++++++++++++++++++++++++++++

//打开数据源
void CNameList::SetupConnect()
{
	try {
		m_DBCnt = NULL;
		m_DBCnt.CreateInstance(__uuidof(Connection));	//建立Connection接口
		_bstr_t sql= "DSN=NameList;";//打开数据源
		m_DBCnt->Open(sql,"","",-1);
	}
	catch(_com_error& e) {
		AfxMessageBox(e.Description());
		this->EndDialog(0);
    }
}

//检查数据的合法性
BOOL CNameList::CheckInputValidity()
{
	if (!UpdateData())
		return FALSE;

	_RecordsetPtr pRst = NULL;	//Recordset的智能指针
	IADORecordBinding   *picRs = NULL;  //VC++ Extensions 接口指针声明（VC++扩展接口）
	CNameListBind  NameBind;

	try {
		TESTHR(pRst.CreateInstance(__uuidof(Recordset)));		//建立Recordset的接口

		//---检查主机名是否已经存在数据库中，如存在就谈出提示，并且直接返回---因为主机名是主键-------------------
		_bstr_t strSQL("SELECT * FROM NameList");	//定义SQL语句
		pRst = m_DBCnt->Execute(strSQL, NULL, adCmdText);		//执行SQL语句

		//建立IADORecordBinding接口
		TESTHR(pRst->QueryInterface(__uuidof(IADORecordBinding),(LPVOID*)&picRs));
		TESTHR(picRs->BindToRecordset(&NameBind));		//绑定到CBook对象book

		while (!pRst->adoEOF)	//获得所有记录
		{
			if ( m_sHostName == NameBind.m_sz_HostName ) {
				AfxMessageBox ( "您输入的主机名已经存在，请重新输入" );
				picRs->Release();
				pRst->Close();
				return FALSE;
			}
			if ( m_sPersonName == NameBind.m_sz_PersonName ) {
				AfxMessageBox ( "您输入的人名已经存在，请重新输入" );
				picRs->Release();
				pRst->Close();
				return FALSE;
			}
			if ( m_sDtmfNo == NameBind.m_sz_DtmfNo ) {
				AfxMessageBox ( "您输入的按键标识码已经存在，请重新输入" );
				picRs->Release();
				pRst->Close();
				return FALSE;
			}
			pRst->MoveNext();
		}
		picRs->Release();
		pRst->Close();
	}
	catch(_com_error& e) {	//异常处理
		AfxMessageBox(e.Description());
		return FALSE;
    }
	return TRUE;
}

//检查输入的完整性
BOOL CNameList::CheckInputIntegrality()
{
	if (!UpdateData())
		return FALSE;
	
	if ( (m_sHostName.GetLength() == 0) || (m_sPersonName.GetLength()==0) 
			|| (m_sDtmfNo.GetLength()==0) || (m_sInLineNo.GetLength()==0) ) {
		AfxMessageBox ( "请把信息填写完整" );
		return FALSE;
	}
	return TRUE;
}




//人名数据库管理操作界面++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

//显示全部
void CNameList::OnShowAll()
{
	m_NameList.DeleteAllItems ();	//先清空列表
	ShowAll();
}

//在列表控件中显示所有的条目
void CNameList::ShowAll()
{
	_RecordsetPtr pRst = NULL;	//Recordset的智能指针
	IADORecordBinding   *picRs = NULL;  //VC++ Extensions 接口指针声明（VC++扩展接口）
	CNameListBind  NameBind;

	try {
		_bstr_t strSQL("SELECT * FROM NameList");	//定义SQL语句

		TESTHR(pRst.CreateInstance(__uuidof(Recordset)));		//建立Recordset的接口
		pRst = m_DBCnt->Execute(strSQL, NULL, adCmdText);		//执行SQL语句

		//建立IADORecordBinding接口
		TESTHR(pRst->QueryInterface(__uuidof(IADORecordBinding),(LPVOID*)&picRs));
		TESTHR(picRs->BindToRecordset(&NameBind));		//绑定到CBook对象book

		//int i = 0;
		while (!pRst->adoEOF)	//获得所有记录
		{
			m_NameList.InsertItem( 0, NameBind.m_sz_HostName );
			m_NameList.SetItemText( 0, 1, NameBind.m_sz_PersonName );
			m_NameList.SetItemText( 0, 2, NameBind.m_sz_DtmfNo );
			m_NameList.SetItemText( 0, 3, NameBind.m_sz_InLineNo );
			pRst->MoveNext();
		}
		picRs->Release();
		pRst->Close();
	}
	catch(_com_error& e) {	//异常处理
		AfxMessageBox(e.Description());
		return;
    }
}

//新增一条记录
void CNameList::OnPersonNew()
{
	if (!UpdateData())
		return;

	if ( !CheckInputIntegrality() ) 
		return;
	
	if ( !CheckInputValidity() ) 
		return;
	
	_RecordsetPtr pRst = NULL;	//Recordset的智能指针
	IADORecordBinding   *picRs = NULL;  //VC++ Extensions 接口指针声明（VC++扩展接口）
	CNameListBind  NameBind;

	try {
		TESTHR(pRst.CreateInstance(__uuidof(Recordset)));		//建立Recordset的接口

		//---------在主机名在数据库中没有的情况下，添加进数据库-------------
		pRst->Open ( "NameList",	//表名
					 _variant_t((IDispatch *) m_DBCnt, true),	//连接
					 adOpenKeyset,								//？？？
					 adLockOptimistic,							//锁定
					 adCmdTable);								//指定执行表操作

		strcpy ( NameBind.m_sz_HostName , m_sHostName );
		strcpy ( NameBind.m_sz_PersonName , m_sPersonName );
		strcpy ( NameBind.m_sz_DtmfNo , m_sDtmfNo );
		strcpy ( NameBind.m_sz_InLineNo , m_sInLineNo );

		COleSafeArray vaFieldlist, vaValuelist;
		NameBind.FillFieldsArray(vaFieldlist,vaValuelist);
		TESTHR(pRst->AddNew(vaFieldlist, vaValuelist));
		pRst->Close();
		//------END---在主机名在数据库中没有的情况下，添加进数据库-------------
	}
	catch(_com_error& e) {	//异常处理
		AfxMessageBox(e.Description());
		return;
    }
	AfxMessageBox ( "完成操作！" );
	m_NameList.DeleteAllItems ();//先清空列表
	ShowAll();
}

//删除一条记录
void CNameList::OnPersonDel()
{
	if (!UpdateData())
		return;
	if ( (m_sHostName.GetLength() == 0) ) {
		AfxMessageBox ( "请选择一条要删除的记录" );
		return;
	}

	CString sql_;
	sql_.Format( "DELETE FROM NameList WHERE HostName='%s'", m_sHostName );
	_bstr_t sql = sql_;

	try	{
		m_DBCnt->Execute(sql,NULL,adCmdText);
	}
	catch(_com_error& e) {
        AfxMessageBox(e.Description());
		return;
    }

	AfxMessageBox ( "完成操作！" );
	m_NameList.DeleteAllItems ();	//先清空列表
	ShowAll();
}

//编辑数据库记录
void CNameList::OnPersonEdit()
{
	if (!UpdateData())
		return;
	if ( !CheckInputIntegrality() ) 
		return;

	_RecordsetPtr pRst = NULL;	//Recordset的智能指针
	IADORecordBinding   *picRs = NULL;  //VC++ Extensions 接口指针声明（VC++扩展接口）
	CNameListBind  NameBind;

	CString sql_;
	//注意：这使用的是以前保存的主机名，因为编辑框里的主机名已经改变
	sql_.Format("SELECT * FROM NameList WHERE HostName='%s'", m_sOldHostName );
	_bstr_t sql = sql_;

	try {
		TESTHR(pRst.CreateInstance(__uuidof(Recordset)));

		pRst->Open(	sql,
					_variant_t((IDispatch *) m_DBCnt, true),
					adOpenKeyset,
					adLockOptimistic,
					adCmdText);

		TESTHR(pRst->QueryInterface(__uuidof(IADORecordBinding),(LPVOID*)&picRs));
		TESTHR(picRs->BindToRecordset(&NameBind));		//绑定信息

		strcpy ( NameBind.m_sz_HostName , m_sHostName );
		strcpy ( NameBind.m_sz_PersonName, m_sPersonName );
		strcpy ( NameBind.m_sz_DtmfNo, m_sDtmfNo );
		strcpy ( NameBind.m_sz_InLineNo, m_sInLineNo );

		TESTHR(picRs->Update(&NameBind));

		picRs->Release();
		pRst->Close();
	}
	catch(_com_error& e) {
		AfxMessageBox(e.Description());
		return;
	}

	AfxMessageBox("完成操作！");
	m_NameList.DeleteAllItems ();	//先清空列表
	ShowAll();
}

//搜索数据库记录
void CNameList::OnPersonSearch()
{
	if (!UpdateData())
		return;

	_RecordsetPtr pRst = NULL;	//Recordset的智能指针
	IADORecordBinding   *picRs = NULL;  //VC++ Extensions 接口指针声明（VC++扩展接口）
	CNameListBind  NameBind;

	_bstr_t sql;
	
	if ( (m_sHostName.GetLength()==0) && (m_sPersonName.GetLength()==0) 
		&& (m_sDtmfNo.GetLength()==0) && (m_sInLineNo.GetLength()==0) ) {	//查询条件全为空的条件下
		AfxMessageBox ( "请至少输入一个查询条件" );
		return;
	}
	
	CString sql_;

	if ( m_sHostName.GetLength()!=0 ) {	//主机名不为空的情况下，按主机名查找
		sql_.Format("SELECT * FROM NameList WHERE HostName='%s'", m_sHostName );
	}
	else if ( (m_sHostName.GetLength()==0)&&(m_sPersonName.GetLength()!=0) ) {	//主机名为空的情况下,人名不为空，按人名查找
		sql_.Format("SELECT * FROM NameList WHERE PersonName='%s'", m_sPersonName );
	}
	else if ( (m_sHostName.GetLength()==0) && (m_sPersonName.GetLength()==0) 
			&& (m_sDtmfNo.GetLength()!=0) ) {
		sql_.Format("SELECT * FROM NameList WHERE DtmfNo='%s'", m_sDtmfNo );
	}
	else if ( (m_sHostName.GetLength()==0) && (m_sPersonName.GetLength()==0) 
			&& (m_sDtmfNo.GetLength()==0) && (m_sInLineNo.GetLength()!=0) ) {
		sql_.Format("SELECT * FROM NameList WHERE InLineNo='%s'", m_sInLineNo );
	}

	sql = sql_;
	m_NameList.DeleteAllItems ();	//先清空列表

	try {
		TESTHR(pRst.CreateInstance(__uuidof(Recordset)));		//建立Recordset的接口
		pRst = m_DBCnt->Execute(sql, NULL, adCmdText);		//执行SQL语句

		//建立IADORecordBinding接口
		TESTHR(pRst->QueryInterface(__uuidof(IADORecordBinding),(LPVOID*)&picRs));
		TESTHR(picRs->BindToRecordset(&NameBind));		//绑定到CBook对象book

		//int i = 0;

		while (!pRst->adoEOF)	//获得所有记录
		{
			//sprintf( buf,"%d",NameBind.m_l_PersonNo );m_NameList.InsertItem( 0, buf );
			m_NameList.InsertItem( 0, NameBind.m_sz_HostName );
			m_NameList.SetItemText( 0, 1, NameBind.m_sz_PersonName );
			m_NameList.SetItemText( 0, 2, NameBind.m_sz_DtmfNo );
			m_NameList.SetItemText( 0, 3, NameBind.m_sz_InLineNo );
			pRst->MoveNext();
		}
		picRs->Release();
		pRst->Close();
	}

	catch(_com_error& e) {	//异常处理
		AfxMessageBox(e.Description());
		return;
    }
}




//----------------写文法到文件里++++++++++++++++++++++++++++++++++++++++++++++++++++++++

//关闭按钮，对话框关闭时要关闭数据库连接，并且把人名写到文法文件里
void CNameList::OnClose()
{
	//setlocale(LC_ALL,"chs");//使用宽字符

	//-------查询所有的记录，然后每条记录生成文法文件-----

	//开始写文件
	CGrammarFile gf( "grammar.xml" );	//建立文法文件，只执行一次
	gf.WriteGraStart();					//写文件头，只执行一次
	BOOL  bWriteTopRule	= FALSE;		//为了只执行一次WriteTopRule()设立的标记

	//读取数据库，并写规则到文件
	_RecordsetPtr pRst = NULL;	//Recordset的智能指针
	IADORecordBinding   *picRs = NULL;  //VC++ Extensions 接口指针声明（VC++扩展接口）
	CNameListBind  NameBind;

	try {
		_bstr_t strSQL("SELECT * FROM NameList");	//定义SQL语句

		TESTHR(pRst.CreateInstance(__uuidof(Recordset)));		//建立Recordset的接口
		pRst = m_DBCnt->Execute(strSQL, NULL, adCmdText);		//执行SQL语句

		//建立IADORecordBinding接口
		TESTHR(pRst->QueryInterface(__uuidof(IADORecordBinding),(LPVOID*)&picRs));
		TESTHR(picRs->BindToRecordset(&NameBind));		//绑定到CBook对象book

		int i = 0;
		while (!pRst->adoEOF) {	//获得所有记录
			gf.WriteDefine ( i+1 );	//写文法定义，执行n次
			pRst->MoveNext();
			i++;
		}

		gf.WriteTopRule();//写顶级规则，只执行一次

		i = 0;
		pRst->MoveFirst();
		while (!pRst->adoEOF)	//获得所有记录
		{
			//写文法规则里的人名，执行n次
			//wchar_t		temp[24];
			//MultiByteToWideChar ( CP_ACP, //把char转换成wchar_t
			//					  0,
			//					  NameBind.m_sz_PersonName,
			//					  sizeof(NameBind.m_sz_PersonName)/sizeof(char),
			//					  temp,
			//					  24 * sizeof( wchar_t ) );

			gf.WriteNameRule( i+1, NameBind.m_sz_PersonName );

			pRst->MoveNext();
			i++;
		}
		picRs->Release();
		pRst->Close();
	}
	catch(_com_error& e) {	//异常处理
		AfxMessageBox(e.Description());
		return;
    }
	gf.WriteGraEnd ();
	//-----end--查询所有的记录，然后每条记录生成文法文件-----
	this->EndDialog(0);
}

