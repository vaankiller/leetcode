#include "list.h"

//version2, change to circle link, then find tail 
struct ListNode* rotateRight(struct ListNode* head, int k) 
{
	if(!head || !head->next)
		return head;

	struct ListNode *cur = head, *newhead = NULL, *pre = NULL;
	int cnt = 1;
	while(cur->next)
	{
		cur = cur->next;
		cnt++;
	}
	k = k%cnt;
	if(k == 0)
		return head;
	else
	{
		cur->next = head;

		cur = head;
		for(int i = 1; i < (cnt-k); i++)
			cur = cur->next;
		newhead = cur->next;
		cur->next = NULL;
	}
	return newhead;
}

//version1, find head, then change
struct ListNode* vrotateRight(struct ListNode* head, int k) 
{
	if(!head || !head->next)
		return head;

	struct ListNode *cur = head, *newhead = NULL, *pre = NULL;
	int cnt = 0;
	while(cur)
	{
		cur = cur->next;
		cnt++;
	}

	k = k%cnt;
	if(k == 0)
		return head;
	else
	{
		cur = head;
		for(int i = 1; i < (cnt-k); i++)
			cur = cur->next;
		pre = cur;
		newhead = pre->next;
		pre->next = NULL;
		cur = newhead;

		while(cur->next)
			cur = cur->next;
		cur->next = head;
	}
	return newhead;
}

void main()
{
	struct ListNode b = {
		.val = 1,
		.next = NULL,
	};

	struct ListNode a = {
		.val = 1,
		.next = &b,
	};
	
	rotateRight(&a, 1);
	return ;
}
	



