#include <stdio.h>
#define bool int
#define true 1
#define false 0
struct TreeNode {

	int val;
	struct TreeNode *left;
	struct TreeNode *right;
};


bool isSameTree(struct TreeNode* p, struct TreeNode* q)
{
	bool ret = false;

	if(p == NULL && q == NULL)
		return true;

	else if(p != NULL && q != NULL)
	{
		if(p->val != q->val)
			return false;

		ret = isSameTree(p->left, q->left)&(isSameTree(p->right, q->right));
		return ret;
	}

	else
		return false;
}


#if 0 //first version
bool isSameTree(struct TreeNode* p, struct TreeNode* q)
{
	bool ret = false;
	if(p == NULL || q == NULL)
		return false;

	if(p->val != q->val)
		return false;
	
	if(p->left == NULL && q->right == NULL)
	{
		return true;
	}

	else if(p->left != NULL && q->left != NULL)
	{
		ret = isSameTree(p->left, q->left);

		if(ret == true)
		{
			if(p->right == NULL && q->right == NULL)
			{
				return true;
			}
			else if(p->right != NULL && q->right != NULL)
			{
				ret = isSameTree(p->right, q->right);
				return ret;
			}

		}
	}
	else
		return false;
}
#endif
