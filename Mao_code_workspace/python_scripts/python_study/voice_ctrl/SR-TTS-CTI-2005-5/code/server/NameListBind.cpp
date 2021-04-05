//////////////////////////////////////////////////////////////////////////////////////////////////
//
// 文件: NameListBind.cpp
//
// 日期：2005年1月21日
//
// 作者: 吕宝虹 (C) All Rights Reserved
//
// 描述: 把数据库中的人员姓名，主机名称这两个字段和要变量进行绑定。供namelist使用。
//
//////////////////////////////////////////////////////////////////////////////////////////////////

#include "SerFrame.h"
#include "stdafx.h"
#include "NameListBind.h"


void CNameListBind::FillFieldsArray(COleSafeArray& vaFieldlist, COleSafeArray& vaValuelist)
{
	vaFieldlist.CreateOneDim( VT_VARIANT, 4 );
	long lArrayIndex[1];
	//lArrayIndex[0] = 0;
	//vaFieldlist.PutElement ( lArrayIndex, &(_variant_t("PersonNo")) );
	lArrayIndex[0] = 0;
    vaFieldlist.PutElement ( lArrayIndex, &(_variant_t("HostName")) );
	lArrayIndex[0] = 1;
	vaFieldlist.PutElement ( lArrayIndex, &(_variant_t("PersonName")) );
	lArrayIndex[0] = 2;
	vaFieldlist.PutElement ( lArrayIndex, &(_variant_t("DtmfNo")) );
	lArrayIndex[0] = 3;
	vaFieldlist.PutElement ( lArrayIndex, &(_variant_t("InLineNo")) );
	

	vaValuelist.CreateOneDim ( VT_VARIANT, 4 );
	//lArrayIndex[0] = 0;
	//vaValuelist.PutElement ( lArrayIndex, &(_variant_t(m_l_PersonNo)) );
	lArrayIndex[0] = 0;
	vaValuelist.PutElement ( lArrayIndex, &(_variant_t(m_sz_HostName)) );
	lArrayIndex[0] = 1;
	vaValuelist.PutElement ( lArrayIndex, &(_variant_t(m_sz_PersonName)) );
	lArrayIndex[0] = 2;
	vaValuelist.PutElement ( lArrayIndex, &(_variant_t(m_sz_DtmfNo)) );
	lArrayIndex[0] = 3;
	vaValuelist.PutElement ( lArrayIndex, &(_variant_t(m_sz_InLineNo)) );
	
}

