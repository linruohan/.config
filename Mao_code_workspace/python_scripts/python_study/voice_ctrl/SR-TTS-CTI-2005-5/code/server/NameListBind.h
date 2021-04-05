//////////////////////////////////////////////////////////////////////////////////////////////////
//
// 文件: NameListBind.h
//
// 日期：2005年1月21日
//
// 作者: 吕宝虹 (C) All Rights Reserved
//
// 描述: 描述: 把数据库中的人员姓名，主机名称这两个字段和要变量进行绑定。供namelist使用。
//
//////////////////////////////////////////////////////////////////////////////////////////////////

#ifndef		LANE_NAMELISTBIND_H
#define		LANE_NAMELISTBIND_H

class CNameListBind : public CADORecordBinding
{
BEGIN_ADO_BINDING(CNameListBind)
    
	//Column empid is the 1st field in the recordset   
	//ADO_VARIABLE_LENGTH_ENTRY2(1, adVarChar, m_l_PersonNo, 
	//							sizeof(m_l_PersonNo), m_sts_PersonNo, TRUE)

	ADO_VARIABLE_LENGTH_ENTRY2(1, adVarChar, m_sz_HostName, 
								sizeof(m_sz_HostName), m_sts_HostName, TRUE)
	
	ADO_VARIABLE_LENGTH_ENTRY2(2, adVarChar, m_sz_PersonName, 
								sizeof(m_sz_PersonName), m_sts_PersonName, TRUE)
	
	ADO_VARIABLE_LENGTH_ENTRY2(3, adVarChar, m_sz_DtmfNo, 
								sizeof(m_sz_DtmfNo), m_sts_DtmfNo, TRUE)
	ADO_VARIABLE_LENGTH_ENTRY2(4, adVarChar, m_sz_InLineNo, 
								sizeof(m_sz_InLineNo), m_sts_InLineNo, TRUE)

END_ADO_BINDING()

public:
	//CHAR	m_l_PersonNo[8];
	CHAR	m_sz_PersonName[12];
	CHAR	m_sz_HostName[64];
	CHAR	m_sz_DtmfNo[10];
	CHAR	m_sz_InLineNo[8];
	
	//ULONG	m_sts_PersonNo;
	ULONG	m_sts_PersonName;
	ULONG	m_sts_HostName;
	ULONG	m_sts_DtmfNo;
	CHAR	m_sts_InLineNo;

public:
	void FillFieldsArray(COleSafeArray& vaFieldlist, COleSafeArray& vaValuelist);
};

#endif		//LANE_NAMELISTBIND_H