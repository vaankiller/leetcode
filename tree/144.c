#include "tree.h"

//version 1, threaded btree, morris algo
int* preorderTraversal(struct TreeNode* root, int* returnSize)
{
	if(!root) 
		return NULL;

	int* arr = (int*)malloc(sizeof(int));
	*returnSize = 0;

	while(root)
	{
		if(!root->left)
		{
			arr = (int*)realloc(arr, sizeof(int)*(++*returnSize));
			arr[*returnSize-1] = root->val;
			root = root->right;
		}
		else
		{
			struct TreeNode* pre = root->left;
			while(pre->right && pre->right!=root)
				pre = pre->right;

			if(!pre->right)
			{
				arr = (int*)realloc(arr, sizeof(int)*(++*returnSize));
				arr[*returnSize-1] = root->val;
				pre->right = root;
				root = root->left;
			}
			else
			{
				pre->right = NULL;
				root = root->right;
			}
		}
	}
	return arr;
}
