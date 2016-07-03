#include "array.h"

int index(unsigned int j)
{
	int i = 31;
	for(i = 31; i >= 0; i--)
	{
		if(j & (1<<i))
			break;
	}
	j = ((j<<(32-i))>>(32-i));
	return j;
}

int* countBits(int num, int* returnSize) {
	*returnSize = num + 1;
	int* ret = malloc(sizeof(int)*(*returnSize));
	if(!ret)
		return NULL;

	ret[0] = 0;        
	if(num == 0)
		return ret;
	else
		ret[1] = 1;
	
	for(int i = 1; (1<<(i)) <= *returnSize; i++)
	{
		for(unsigned int j = (1<<i); j < *returnSize && j < (1<<(i+1)); j++)
		{
			ret[j] = ret[index(j)] + 1;
		}
		for(int k = 0; k < *returnSize; k++)
			printf("%d,", ret[k]);
		puts("");
	}
	return ret;
}

void main()
{
	int *size = malloc(sizeof(int));
	int i = 0;
	int *nums = NULL;

	nums = countBits(4, size);
	for(i = 0; i < *size; i++)
		printf("%d,", nums[i]);

	return ;
}
