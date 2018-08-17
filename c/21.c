#include <stdio.h>
#include <string.h>

#define bool int
#define true 1
#define false 0

struct ListNode {
	int val;
	struct ListNode *next;
};


struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2)
{
	if(!l1 && !l2)
		return NULL;

	if(!l1 || !l2)
		return l1 != NULL?l1:l2;

	struct ListNode *pcur1 = l1, *pcur2 = l2, *pcur, *newhead;

	if(l1->val < l2->val)
	{
		newhead = l1;
		pcur1 = l1->next;
	}
	else
	{
		newhead = l2;
		pcur2 = l2->next;
	}
	
	pcur = newhead;
	while(pcur1 && pcur2)
	{
		if(pcur1->val < pcur2->val)
		{
			pcur->next = pcur1;
			pcur1 = pcur1->next;
		}
		else
		{
			pcur->next = pcur2;
			pcur2 = pcur2->next;
		}
		pcur = pcur->next;
	}
	pcur->next = pcur1?pcur1:pcur2;
	return newhead;
}


//version 3 self recursive
struct ListNode* rmergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
	if(!l1 && !l2)
		return NULL;

	if(!l1 || !l2)
		return l1?l1:l2;

	if(l1->val < l2->val)
	{
		l1->next = mergeTwoLists(l1->next, l2);
		return l1;
	}
	else
	{
		l2->next = mergeTwoLists(l1, l2->next);        
		return l2;
	}
}



//version 2 : answer recursive , studying
#if 0
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2)
{
	if (l1 == NULL)  
		return l2;  
	if (l2 == NULL)  
		return l1;  
	if (l1->val < l2->val)  
	{
		l1->next = mergeTwoLists(l1->next,l2);  
		return l1;  
	}
	else  
	{
		l2->next = mergeTwoLists(l1,l2->next);  
		return l2;  
	}
}
//version 1 : cannot pass, because time limit exceed, i do not konw why
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2)
{
	struct ListNode *pl1 = l1;
	struct ListNode *pl2 = l2;
	struct ListNode *l = (struct ListNode*)malloc(sizeof(struct ListNode*)) ;
	struct ListNode *pcur = l;

	if(l1 == NULL || l2 == NULL)
		l = l1?l1:l2;

	while(pl1 && pl2)
	{
		pcur->next = (struct ListNode*)malloc(sizeof(struct ListNode*));
		if(pl1->val < pl2->val)
		{
			pcur->val = pl1->val;
			pl1 = pl1->next;
		}
		else
		{
			pcur->val = pl2->val;
			pl2 = pl2->next;
		}
		pcur = pcur->next;
	}

	pcur = pl1?pl1:pl2;
	return l;      
}
#endif

void main()
{
	struct ListNode a = {
		.val = 6,
		.next = NULL,
	};
	
	struct ListNode b = {
		.val = 8,
		.next = NULL,
	};

	struct ListNode c = {
		.val = 5,
		.next = &b,
	};

	struct ListNode *head = mergeTwoLists(&a, &c);
	while(head)
	{
		printf("%d,",head->val);
		head = head->next;
	}
	return ;
}

