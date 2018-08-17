#include "list.h"

struct TreeNode* sortedListToBST(struct ListNode* head) 
{
	if(!head)
		return NULL;
	else if(!head->next)
	{   
		struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
		root->val = head->val;
		root->left = NULL;
		root->right = NULL;
		return root;
	}   

	struct ListNode *slow = head, *fast = head, *prv;
	while(fast && fast->next)
	{   
		prv = slow;
		slow = slow->next;
		fast = fast->next->next;
	}   

	struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));

	prv->next = NULL;
	root->val = slow->val;

	root->left = sortedListToBST(head);
	root->right = sortedListToBST(slow->next);

	return root;
}

void main()
{
	struct ListNode;
}

