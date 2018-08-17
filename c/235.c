
#include "tree.h"

struct treeNode* lowestCommonAncestor(struct treeNode* root, struct treeNode* p, struct treeNode* q) {

	if(!root || !p || !q)
		return NULL;
	else if(p->val == q->val)
		return p;
	else if((p->val <= root->val && q->val >= root->val) || (p->val >= root->val && q->val <= root->val))
		return root;
	else if(p->val < root->val && q->val < root->val)
		return lowestCommonAncestor(root->left, p, q);
	else if(p->val > root->val && q->val > root->val)
		return lowestCommonAncestor(root->right, p, q);
}


void main()
{
	struct treeNode	a = {
		.val = 2,
		.left = NULL,
		.right = NULL,
	};

	struct treeNode	b = {
		.val = 1,
		.left = NULL,
		.right = NULL,
	};

	struct treeNode	c = {
		.val = 3,
		.left = NULL,
		.right = NULL,
	};

	a.left = &b;
	a.right = &c;
	struct treeNode* p = &b;
	struct treeNode* q = &c;
	struct treeNode* ret = NULL;

	ret = lowestCommonAncestor(&a,p,q);
	printf("%d\n", ret->val);
}
