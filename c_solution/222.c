#include "tree.h"

int countNodes(struct TreeNode* root) {
	if(!root)
		return 0;

	struct TreeNode *l = root, *r = root;
	int depth = 0;

	for(; l && r; depth++)
	{
		l = l->left;
		r = r->right;
	}

	if(!l && !r) return (1<<depth) -1;

	return countNodes(root->left) + 1 + countNodes(root->right);
}
