#include "list.h"
//version2

struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) 
{
	if (listsSize < 0) 
		return 0;
	if (listsSize == 1) 
		return lists[0];

	int i, idx = 0;
	for (i = 0; i < listsSize; ) 
	{
		if (i + 1 < listsSize) 
		{
			lists[idx++] = mergeTwoLists(lists[i], lists[i + 1]);
			i += 2;
		}
		else lists[idx++] = lists[i++];
	}
	return mergeKLists(lists, idx);
}

//versoin 1, time limited exceed, everytime merge one time, not effective
struct ListNode* mergeKLists(struct ListNode** lists, int listsSize)
{
	if(listsSize <= 0)
		return 0;
	else if(listsSize == 1)
		return lists[0];
	else if(listsSize == 2)
		return mergeTwoLists(lists[0], lists[1]);
	else
	{
		lists[listsSize-2] = mergeTwoLists(lists[listsSize-2], lists[listsSize-1]);
		return mergeKLists(lists, listsSize-1);
	}
	return lists[0];
}
