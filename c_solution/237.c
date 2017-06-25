#include <stdio.h>
#include <stdlib.h>
#define bool int
#define true 1
#define false 0

struct ListNode {
	int val;
	struct ListNode *next;
};

void deleteNode(struct ListNode* node) {
	if(node == NULL)
		return NULL;
	while(node->next)
	{
		node->val = node->next->val;
		if(node->next->next == NULL)
		{
			node->next = NULL;
			return node;
		}
		else
			node = node->next;
	}
}
