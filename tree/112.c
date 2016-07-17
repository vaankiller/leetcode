#include "tree.h"

bool hasPathSum(struct TreeNode* root, int sum) {
	if(root == NULL)
		return false;

	if(!root->left && !root->right && root->val == sum)
		return true;
	else if(root->left && root->right)
		return hasPathSum(root->left, sum-root->val) | hasPathSum(root->right, sum-root->val);
	else if(root->right)
		return hasPathSum(root->right, sum-root->val);
	else if(root->left)
		return hasPathSum(root->left, sum-root->val);
	else
		return false;
}

