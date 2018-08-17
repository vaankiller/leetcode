#include "tree.h"

struct TreeNode* invertTree(struct TreeNode* root) {
	if(root == NULL)
		return NULL;

	struct TreeNode* tmp = NULL;
	tmp = root->left;
	root->left = root->right;
	root->right = tmp;

	invertTree(root->left);
	invertTree(root->right);

	return root;
}
