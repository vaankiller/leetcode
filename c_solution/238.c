#include "array.h"

int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
	int product = 1, cnt_zero = 0, idx_zero = 0;
	int* ret = malloc(sizeof(int)*numsSize);
	*returnSize = numsSize;

	for(int i = 0; i < numsSize; i++)
	{
		if(nums[i] == 0)
		{
			if(cnt_zero == 0)
			{
				idx_zero = i;
				cnt_zero++;
				continue;
			}
			else
				return ret;
		}
		product *= nums[i];
	}
	if(cnt_zero == 1)
	{
		ret[idx_zero] = product;
		return ret;
	}
	else
	{
		for(int i = 0; i < numsSize; i++)
			ret[i] = product / nums[i];
	}
	return ret;
}


void main()
{
	int test[4] = {1,2,3,4};
	int a = 0;
	int *ret = NULL;
	ret = productExceptSelf(test, 4, &a);
	for(int i = 0; i < 4; i++)
		printf("%d,", ret[i]);

	return ;
}
