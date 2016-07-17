#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int minDepth(struct TreeNode* root) {
	if(!root)
		return 0;
	if(root->left == NULL && root->right == NULL)
		return 1;
	else if(root->left && root->right)
		return minDepth(root->left)+1>minDepth(root->right)+1?minDepth(root->right)+1:minDepth(root->left)+1;
	else if(root->left)
		return minDepth(root->left)+1;
	else if(root->right)
		return minDepth(root->right)+1;
}
