#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define bool int
#define true 1
#define false 0

struct ListNode* oddEvenList(struct ListNode* head);
struct ListNode {
	int val;
	struct ListNode *next;
};

void main()
{
	int i = 0;
	struct ListNode a = {
		.val = 1,
		.next = NULL,
	};
	
	struct ListNode b = {
		.val = 2,
		.next = NULL,
	};

	struct ListNode c = {
		.val = 3,
		.next = NULL,
	};

	struct ListNode d = {
		.val = 4,
		.next = NULL,
	};

	a.next = &b;
	b.next = &c;
	c.next = &d;

	oddEvenList(&a);
	return;
}
struct ListNode* oddEvenList(struct ListNode* head)
{
	if(head == NULL || head->next == NULL || head->next->next == NULL)
		return head;

	struct ListNode*  tmp= head->next;    
	struct ListNode* podd = head;    
	struct ListNode* peven = head->next;

	while(podd->next->next)
	{

		podd->next = podd->next->next;
		podd = podd->next;

		peven->next = peven->next->next;
		peven = peven->next; 

		if(podd->next)
			break;
	}
	podd->next = tmp;
	return head;
}
