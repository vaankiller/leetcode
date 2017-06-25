#include "tree.h"


struct TreeNode* vsortedArrayToBST(int* nums, int start, int end)
{
	struct TreeNode* root = malloc(sizeof(struct TreeNode));
	root->val = nums[(end-start)/2+start];

	if(start == end)
	{
		root->left = NULL;
		root->right = NULL;
	}
	else if(end - start == 1)
	{
		root->left = NULL;
		root->right = vsortedArrayToBST(nums, start+(end-start)/2+1,end);
	}
	else
	{
		root->left = vsortedArrayToBST(nums, start, start+(end-start)/2-1);
		root->right = vsortedArrayToBST(nums, start+(end-start)/2+1,end);
	}
	return root;
}

struct TreeNode* sortedArrayToBST(int* nums, int numsSize) 
{
	if(!nums || numsSize == 0)
		return NULL;
	else
		return vsortedArrayToBST(nums, 0, numsSize-1);
}



void main()
{
	int test[3] = {1,2,3};
	struct TreeNode* root = sortedArrayToBST(test, 3);
	printf("%d,%d,%d\n", root->val, root->left->val, root->right->val);

}
