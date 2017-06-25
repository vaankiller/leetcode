#include "list.h"
//version 2 clean easy to understand 
struct ListNode* deleteDuplicates(struct ListNode* head) {
	if(head == NULL || head->next == NULL)
		return head;

	struct ListNode* nxt = head->next;

	if(head->val != nxt->val)
		head->next = deleteDuplicates(head->next);
	else
	{
		while(nxt->next && nxt->next->val == head->val)
			nxt = nxt->next;

		if(!nxt->next)
			return NULL;
		else
			return deleteDuplicates(nxt->next);
	}
	return head;
}

//funny quiz,in the board ,three condition in if judgement,
//spent lots of time
//one:recursive two:no recursive
struct ListNode* deleteDuplicates(struct ListNode* head) {

	if(head == NULL || head->next == NULL)
		return head;

	struct ListNode* cur = head;
	struct ListNode* nxt = head->next;

	if(cur->val != nxt->val)
		cur->next = deleteDuplicates(cur->next);
	else if(cur->next->next == NULL && cur->val == nxt->val)
		return NULL;
	else 
	{
		while(nxt->next)
		{
			if(cur->val == nxt->val)
			{
				nxt = nxt->next;
				if(nxt->next == NULL && nxt->val == cur->val)
					return NULL;
			}
			else
				break;
		}
		head = deleteDuplicates(nxt);
	}
	return head;
}
