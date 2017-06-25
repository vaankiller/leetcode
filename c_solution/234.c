#include <stdio.h>
#include <stdlib.h>
#define bool int
#define true 1
#define false 0

struct ListNode {
	int val;
	struct ListNode *next;
};

bool isPalindrome(struct ListNode* head) {
	if(!head || !head->next)
		return true;

	struct ListNode *slower = head, *faster = head, *middle = NULL;
	while(faster && faster->next)
	{
		slower = slower->next;
		faster = faster->next->next;
	}

	while(slower)
	{
		struct ListNode * next;

		next = slower->next;
		slower->next = middle;
		middle = slower;
		slower = next;
	}

	struct ListNode *cur = head, *rev = middle;
	for(; cur->next && rev->next; rev=rev->next, cur=cur->next)
	{
		if(cur->val != rev->val)
			return false;
	}
	return true;
}

#if 0 


//version 2 save a list to stack then compare it
bool isPalindrome(struct ListNode* head) 
{
	struct ListNode *cur = head;

	if(head == NULL || head->next == NULL)
		return true;
	
	struct ListNode *addr = malloc(sizeof(struct ListNode*));

	while(cur->next != NULL)
	{
		addr->next = malloc(sizeof(struct ListNode*));
		addr->next = addr;
		addr = cur;
		cur = cur->next;
	}

	struct ListNode *tmp = addr;
	cur = head;
	while(tmp->next != NULL)
	{
		if(tmp->val != cur->val)
			return false;
		else
		{
			tmp = tmp->next;
			cur = cur->next;
		}	
	}
	return true;
}

#if 0 // version time limit the main reason is recursive,evervtime need to travel the link list
	  //tip : tail recursion ; remove recursion by goto
bool isPalindrome(struct ListNode* head) 
{
	struct ListNode *tail = head;

	if(head == NULL || head->next == NULL)
		return true;

	while(tail->next->next != NULL)
		tail = tail->next;

	if(tail->next->val != head ->val)
		return false;
	else
		tail->next = NULL;

	return isPalindrome(head->next);
}
#endif
