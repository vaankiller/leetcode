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

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2)
{
	if(!l1 && !l2)
		return NULL;
	else if(!l1 || !l2)
		return l1?l1:l2;

	int v1 = 0, v2 = 0, sum = 0, carry = 0;

	struct ListNode* head = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode* current = head;

	while (l1 || l2 || carry)
	{
		v1 = (l1 == NULL)? 0 : l1->val;
		v2 = (l2 == NULL)? 0 : l2->val;

		sum = v1 + v2 + carry;
		carry = sum / 10;
		sum %= 10;

		struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
		newNode->val = sum;
		newNode->next = NULL;

		current->next = newNode;
		current = current->next;

		l1 = (l1 == NULL)? l1 : l1->next;
		l2 = (l2 == NULL)? l2 : l2->next;
	}
	return head->next;
}


void main()
{
	struct ListNode a;
	a.val = 1;
	a.next = NULL;


	struct ListNode c;
	c.val = 9;
	c.next = NULL;

	struct ListNode b;
	b.val = 1;
	b.next = &c;

	struct ListNode* sum = addTwoNumbers(&a,&b);
	while(sum)
	{
		printf("%d,", sum->val);
		sum = sum->next;
	}
	puts("");
	return ;
}






//version2, please read the question carefully...
//although ...
/*
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


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) 
{
	if(!l1 && !l2)
		return NULL;
	else if(!l1 || !l2)
		return l1?l1:l2;

	struct ListNode *p1 = l1;
	struct ListNode *p2 = l2;
	int cnt1 = 1, cnt2 = 1;
	while(p1->next)
	{
		p1 = p1->next;
		++cnt1;
	}
	while(p2->next)
	{
		p2 = p2->next;
		++cnt2;
	}

	if(cnt1 < cnt2)
		return addTwoNumbers(l2, l1);

	p1 = reverseList(l1);
	p2 = reverseList(l2);
	struct ListNode *newhead = p1;
	int c = 0;
	
	while(p1 && p2)
	{
		p1->val = p1->val + p2->val + c;
		if(p1->val >= 10)
		{
			p1->val %= 10;
			c = 1;
		}
		else
			c = 0;
		p1 = p1->next;
		p2 = p2->next;
	}
	if(!p1)
	{
		if(c == 1)
		{
			struct ListNode* f = malloc(sizeof(struct ListNode));
			f->val = 1;
			f->next = NULL;
			p1->next = f;
		}
		return reverseList(p1);
	}
	else
	{
		while(p1)
		{
			p1->val += c;
			if(p1->val >= 10)
			{
				p1->val %= 10;
				c = 1;
			}
			else
				c = 0;
			p1 = p1->next;
		}
		if(c == 1)
		{
			struct ListNode* f = malloc(sizeof(struct ListNode));
			f->val = 1;
			f->next = NULL;
			p1->next = f;
		}
		return reverseList(newhead);
	}
}
*/

#if 0 
// version one fucking >=10 not >10 cost 0.5h and kind of error 
// because u didn't even thinking,just code it down, crap!
// the direction wrong, from end to start,... reverse first
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
	int c = 0;
	struct ListNode* pl1 = l1;
	struct ListNode* pl2 = l2;
	struct ListNode* sum = (struct ListNode*)malloc(sizeof(struct ListNode*));
	struct ListNode* pcur = sum;
	if(!sum)
		return NULL;

	while(pl1 && pl2)
	{
		pcur->val = pl1->val + pl2->val + c;
		if(pcur->val >= 10)
		{
			c= 1;
			pcur->val = pcur->val % 10;
		}
		else
			c = 0;
		pcur->next = (struct ListNode*)malloc(sizeof(struct ListNode*));
		pl1 = pl1->next;
		pl2 = pl2->next;
		pcur = pcur->next;
	}

	if(pl1 == NULL && pl2 != NULL)
	{
		pcur = pl2;
		pcur->val += c;
		while(pcur->val >= 10)
		{

			pcur->val %= 10;
			c = 1;
			printf("%d\n",pcur->val);
			if(pcur->next == NULL)
			{
				puts("last");
				pcur->next = (struct ListNode*)malloc(sizeof(struct ListNode*));
				pcur->next->val = 1;
				pcur->next->next = NULL;
				break;
			}
			else
			{
				pcur->next->val += c;
			}
			pcur = pcur->next;
		}
	}
	else if (pl1 != NULL && pl2 == NULL)
	{
		puts("1");
		pcur = pl1;
		pcur->val += c;
		while(pcur->val >= 10)
		{

			pcur->val %= 10;
			c = 1;
			if(pcur->next == NULL)
			{
				pcur->next = (struct ListNode*)malloc(sizeof(struct ListNode*));
				pcur->next->val = 1;
			}
			else
			{
				pcur->next->val += c;
			}
			pcur = pcur->next;
		}
	}
	else
	{
		puts("0");
		if(c)
		{

			pcur->val = c;
			pcur->next = NULL;
		}
	}
	return sum;
}
#endif
