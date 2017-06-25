#include "list.h"

struct RandomListNode* copyRandomList(struct RandomListNode *head)
{
	if(!head) return NULL;
	struct RandomListNode *newHead=NULL, *oldNode=head, *newNode=NULL;
	while(oldNode) 
	{
		newNode = (struct RandomListNode*)malloc(sizeof(struct RandomListNode));
		newNode->next = oldNode->next;
		newNode->label = oldNode->label;
		newNode->random = NULL;
		oldNode->next = newNode;
		oldNode = oldNode->next->next;
	}
	oldNode = head;
	while(oldNode)
	{
		if(oldNode->random)
			oldNode->next->random = oldNode->random->next;
		oldNode = oldNode->next->next;
	}

	newHead = head->next;
	newNode = head->next;
	oldNode = head;
	while(oldNode) 
	{
		oldNode->next = oldNode->next->next;
		if(oldNode->next == NULL)
		{
			newNode->next = NULL;
			break;
		}
		newNode->next = newNode->next->next;
		newNode = newNode->next;
		oldNode = oldNode->next;
	}
	return newHead;
}
