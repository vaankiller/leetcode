#include <stdio.h>
#include <stdlib.h>
#define bool int
#define true 1
#define false 0

struct ListNode {
	int val;
	struct ListNode *next;
};

struct ListNode* deleteDuplicates(struct ListNode* head) {
	if(head == NULL || head->next == NULL)
		return head;

	struct ListNode* pcur = head->next;
	struct ListNode* pfix = head;

	while(pcur != NULL)
	{
		if(pcur->val == pfix->val)
			pfix->next = pfix->next->next;
		else
			pfix = pcur;
		pcur = pcur->next;
	}
	return head;
}
