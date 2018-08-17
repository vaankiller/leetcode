

int maxDepth(struct TreeNode* root) {
	if(root == NULL)
		return 0;
	int leftDepth = 0;
	int rightDepth = 0;

	leftDepth = maxDepth(root->left) + 1;
	rightDepth = maxDepth(root->right) + 1;
	return leftDepth>rightDepth?leftDepth:rightDepth;
}
