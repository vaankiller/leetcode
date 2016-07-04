#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define bool int
#define true 1
#define false 0

struct ListNode {
	int val;
	struct ListNode *next;
};

struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
	if(head == NULL || head->next == NULL)
		return NULL;
	struct ListNode *first = head;
	struct ListNode *second = head;

	for(int i = 0; i < n; ++i)
	{
		first = first->next;
	}

	if(first == NULL)
		return head->next;
	
	while(first->next)
	{
		first = first->next;
		second = second->next;
	}
	second->next = second->next->next;
	return head;
}
// version 1 use three ptrs not two ,
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
	if(head == NULL || head->next == NULL)
		return NULL;

	struct ListNode *pre = head;
	struct ListNode *cur = head;
	struct ListNode *tmp = NULL;
	int i = 0;

	while(i < n-1)
	{
		pre = pre->next;
		i++;
	}
	while(pre->next)
	{
		tmp = cur;
		cur = cur->next;
		pre = pre->next;
	}
	if(cur == head)
		head = cur->next;
	else
		tmp->next = tmp->next->next;
	return head;
}
