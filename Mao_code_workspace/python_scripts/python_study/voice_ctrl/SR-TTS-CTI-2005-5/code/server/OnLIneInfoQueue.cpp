// OnLIneInfoQueue.cpp: implementation of the COnLIneInfoQueue class.
//
//////////////////////////////////////////////////////////////////////

#include "stdafx.h"
#include "SerFrame.h"
#include "OnLIneInfoQueue.h"

#ifdef _DEBUG
#undef THIS_FILE
static char THIS_FILE[]=__FILE__;
#define new DEBUG_NEW
#endif

//////////////////////////////////////////////////////////////////////
// Construction/Destruction
//////////////////////////////////////////////////////////////////////
COnLIneInfoQueue::COnLIneInfoQueue():UserNumber(0),CurrenPos(0)
{
	Head=NULL;
	TailElement=NULL;
}

COnLIneInfoQueue::~COnLIneInfoQueue()
{
	COnlineInfoItem *cur;
	cur=Head;
	if(UserNumber==0)
	while((UserNumber!=0)&&((cur->next)!=NULL))
	{
		Head=cur->next;
		delete cur;	
		cur=Head;
	}
	if(UserNumber!=0)
	delete Head;
}
void COnLIneInfoQueue::AddItem(COnlineInfoItem item)
{
	if(Head==NULL)//在队列的头部加入元素
	{
		Head=new COnlineInfoItem;
		*Head=item;
		UserNumber++;
		TailElement=Head;
		Head->next=NULL;
		TailElement->next=NULL;
	}                         
	else
	{
		COnlineInfoItem *NewItem=new COnlineInfoItem;
		*NewItem=item;
		UserNumber++;
		TailElement->next=NewItem;
		TailElement=NewItem;
		TailElement->next=NULL;
	}
}
COnlineInfoItem& COnLIneInfoQueue::operator[](int elem)
{
	COnlineInfoItem *ReturnValue;
	if(UserNumber==0)
	{
		TRACE("\nCOnLIneInfoQueue错误，队列中还没有元素\n");
	}
	if(elem>UserNumber-1)
	{
		TRACE("\nCOnLIneInfoQueue错误，超出了遍历范围\n");
	}
	int i=0;
	ReturnValue=Head;
	while(i!=elem)
	{
		ReturnValue=ReturnValue->next;
		i++;
	}
	return *ReturnValue;
}
bool COnLIneInfoQueue::SearchItemByUserName(CString UserName,int *pos)
{
	COnlineInfoItem *cur;
	int i=0;
	cur=Head;
	while(cur!=NULL)
	{
		if((cur->GetUserName())==UserName)
		{
			*pos=i;
			return true;
		}
		cur=cur->next;
		i++;
	}
	return false;
}
void COnLIneInfoQueue::DeleteItem(int pos)
{
	COnlineInfoItem *prior, *cur;
	int i=0;
	if(pos==0)
	{
		cur=Head->next;
		delete Head;
		Head=cur;
	}
	else
	{
		cur=Head;
		while(i!=pos && cur != NULL )
		{
			i++;
			prior=cur;
			cur=cur->next;
		}
		
		if ( cur ) 
		{
			prior->next=cur->next;
			delete cur;
		}

		//delete cur;
	}	
	UserNumber--;
	SetTailPoint();
	
}
void COnLIneInfoQueue::PrintQueue()
{
	COnlineInfoItem *cur;
	cur=Head;
	while(cur!=NULL)
	{
		TRACE("username: %s\n",cur->GetUserName());
		TRACE("ip: %s\n",cur->GetIP());
		TRACE("headID: %d\n",cur->GetHeadID());
		TRACE("Port: %d\n\n",cur->GetListenPort());	
		cur=cur->next;
	}
}
void COnLIneInfoQueue::SetTailPoint()
{
	COnlineInfoItem *cur;
	cur=Head;
	if(cur==NULL)
	{
		TailElement=Head;
		return;
	}
	while((cur->next)!=NULL)
	{
		cur=cur->next;
	}
	TailElement=cur;
}