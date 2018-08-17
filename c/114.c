#include "tree.h"

struct TreeNode* traverseLeft(struct TreeNode* root)
{
	if(!root->left &&!root->right) return root;

	struct TreeNode* t = root->right;
	root->right = root->left;

	struct TreeNode *leftmost = root; 
	if(root->left)
		leftmost = traverseLeft(root->left);
	root->left = NULL;

	leftmost->right = t;
	if(t) traverseLeft(t); 
}

void flatten(struct TreeNode* root)
{
	if(!root) return ;
	traverseLeft(root);
}
