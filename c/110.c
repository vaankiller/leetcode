

bool isBalanced(struct TreeNode* root) {
	if(!root)
		return true;

	int height = maxDepth(root->left) - maxDepth(root->right);
	if(height == 0 || height == 1 || height == -1)
		return isBalanced(root->left) && isBalanced(root->right);
	else
		return false;
}

int maxDepth(struct TreeNode* root) {
	if(root == NULL)
		return 0;
	int leftDepth = 0;
	int rightDepth = 0;

	leftDepth = maxDepth(root->left) + 1;
	rightDepth = maxDepth(root->right) + 1;
	return leftDepth>rightDepth?leftDepth:rightDepth;
}
