#include "tree.h"

//version 1 recursive
bool symmetric( struct TreeNode* left, struct TreeNode* right )
{
	if(!left && !right) 
		return true;
	else if(!left || !right) 
		return false;
	if(left->val != right->val) 
		return false;

	return symmetric(left->left, right->right) && symmetric(left->right, right->left);
}

bool isSymmetric( struct TreeNode * root )
{
	if(!root) 
		return true;
	return symmetric(root->left, root->right);
}

//version 2 norecursive
struct TreeNode** fillNext( struct TreeNode** stack, int size , int* newSize)
{
	struct TreeNode** t = ( struct TreeNode** )malloc(sizeof( struct TreeNode* )*2*size);
	int index = 0;
	for(int i = 0; i < size; i++)
	{
		if(stack[i])
		{
			t[index++] = stack[i]->left;
			t[index++] = stack[i]->right;
		}
	}
	*newSize = index;
	return t;
}

bool isSymmetric( struct TreeNode * root )
{
	if(!root || (!(root->left) && !(root->right))) 
		return true;
	if(!root->left || !root->right) 
		return false;

	int count = 1;
	struct TreeNode **lStack = (struct TreeNode**)malloc(sizeof(struct TreeNode*));
	struct TreeNode **rStack = (struct TreeNode**)malloc(sizeof(struct TreeNode*));
	lStack[0] = root->left;
	rStack[0] = root->right;

	while(count)
	{
		int lIndex = 0, rIndex = 0;
		for(int i = 0; i < count; i++)
		{
			if(!lStack[i] || !rStack[count-i-1])
			{
				if(!lStack[i] && !rStack[count-i-1])
					continue;
				return false;
			}
			if(lStack[i]->val != rStack[count-i-1]->val)
				return false;
		}
		int lCount=0, rCount=0;
		lStack = fillNext(lStack, count, &lCount);
		rStack = fillNext(rStack, count, &rCount);
		if(lCount != rCount) return false;
		count = lCount;
	}
	return true;
}
