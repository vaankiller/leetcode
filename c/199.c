#include "tree.h"

//version1 think too less
/*
int* rightSideView(struct TreeNode* root, int* returnSize) {
	if(!root)
		return NULL;

	int* ret = malloc(sizeof(int) * 1024);
	int cnt = 0;
	ret[0] = root->val;
	struct TreeNode* pcur = root;

	while(pcur->right || pcur->left)
	{
		if(pcur->right)
			pcur = pcur->right;
		else
			pcur = pcur->left;
		ret[++cnt] = pcur->val;
	}
	*returnSize = cnt+1;
	return ret;    
}
*/
void main()
{
	struct TreeNode root;
	struct TreeNode root1;
	root.val = 1;
	root.left = &root1;
	root.right = NULL;

	root1.val = 2;
	root1.left = NULL;
	root1.right = NULL;
	int a = 0;
	int *p = NULL;
	p = rightSideView(&root, &a);
	printf("%d, %d\n", p[1], a);
}
