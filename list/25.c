#include "list.h"

struct ListNode* reverseList(struct ListNode* head) {
	if(head == NULL || head->next == NULL)
		return head;

	struct ListNode* pre = NULL;
	struct ListNode* pcur = head;
	struct ListNode* next;

	while(pcur)
	{
		next = pcur->next;
		pcur->next = pre;
		pre = pcur;
		pcur = next;
	}
	return pre;
}

struct ListNode* reverseKGroup(struct ListNode* head, int k) {
	if(!head || !head->next || k <= 1)
		return head;

	struct ListNode *cur = head, *tail = head, *next, *newhead;
	int cnt = 1;

	for(cnt = 1; cur->next && cnt < k+1; cnt++)
		cur = cur->next;

	if(!cur->next && cnt != k)
		return head;
	else
	{
		next = cur->next;
		cur->next = NULL;

		newhead = reverseList(head);
		tail->next = reverseKGroup(next, k);
	}
	return newhead;    
}


void main()
{
	struct ListNode a = {
		.val = 2,
		.next = NULL,
	};

	struct ListNode b = {
		.val = 1,
		.next = &a,
	};

	reverseKGroup(&b, 2);
	return;
}
