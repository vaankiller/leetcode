#include <stdio.h>
#include <stdlib.h>
#define bool int
#define true 1
#define false 0

struct ListNode {
	int val;
	struct ListNode *next;
};

struct ListNode* reverseList(struct ListNode* head)
{
	if(head == NULL || head->next == NULL)
		return head;

	struct ListNode* tail = head->next;
	struct ListNode* newhead = reverseList(head->next);

	tail->next = head;
	head->next = NULL;

	return newhead;
}

struct ListNode* reverseList(struct ListNode* head) 
{
	if(!head || head->next)
		return head;

	struct ListNode *prev = NULL, *next;
	while(head)
	{
		next=head->next;
		head->next=prev;
		prev=head;
		head=next;
	}
	return prev;

}
