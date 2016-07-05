#include <stdio.h>
#include <stdlib.h>
#define bool int
#define true 1
#define false 0

struct ListNode {
	int val;
	struct ListNode *next;
};

//version 1
struct ListNode* removeElements(struct ListNode* head, int val) {
	if(head == NULL)
		return NULL;

	struct ListNode* pcur = head;

	while(pcur->val == val)
	{
		head = head->next;
		pcur = head;
		if(pcur == NULL)
			return pcur;
	}

	while(pcur->next != NULL)
	{
		if(pcur->next->val == val)
			pcur->next = pcur->next->next;
		else
			pcur = pcur->next;
	}
	return head;
}
