// OnLIneInfoQueue.h: interface for the COnLIneInfoQueue class.
//
//////////////////////////////////////////////////////////////////////

#if !defined(AFX_ONLINEINFOQUEUE_H__B2820C13_2444_4082_8133_5DDD6646D81A__INCLUDED_)
#define AFX_ONLINEINFOQUEUE_H__B2820C13_2444_4082_8133_5DDD6646D81A__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000
#include "OnlineInfoItem.h"

class COnLIneInfoQueue  
{
public:
	COnLIneInfoQueue();
	virtual ~COnLIneInfoQueue();
    
    int CurrenPos;//用来记录当前游标指向队列的什么位置。
    int UserNumber;
    
    void AddItem(COnlineInfoItem item);
    COnlineInfoItem& operator[](int elem);
    bool SearchItemByUserName(CString UserName,int *pos);
    void DeleteItem(int pos);
    void PrintQueue();//用于测试中
    
private:
    COnlineInfoItem *Head;
    COnlineInfoItem *TailElement;
    void SetTailPoint();//在删除中可能会破坏队列的尾巴，所以要重新设置一下。
};

#endif // !defined(AFX_ONLINEINFOQUEUE_H__B2820C13_2444_4082_8133_5DDD6646D81A__INCLUDED_)
