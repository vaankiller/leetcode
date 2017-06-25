#include "tree.h"

bool isNodeInTree(struct TreeNode* root, struct TreeNode* node)
{
	if(!root || !node)
		return false;

	if(root == node)
		return true;
	else
		return isNodeInTree(root->left, node) || isNodeInTree(root->right, node);
}

struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
	if(!root || !p || !q)
		return NULL;

	if(isNodeInTree(p, q))
		return p;
	else if(isNodeInTree(q, p))
		return q;

	if(isNodeInTree(root->left, p) && isNodeInTree(root->left, q))
		return lowestCommonAncestor(root->left, p, q);
	else if(isNodeInTree(root->right, p) && isNodeInTree(root->right, q)) 
		return lowestCommonAncestor(root->right, p, q);
	else
		return root;
}
