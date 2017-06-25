#include <stdio.h>

int* twoSum(int* nums, int numsSize, int target) {
	int i,j;
	int *ret = malloc(sizeof(int)*2);

	for(i = 0; i < numsSize; i++)
	{
		for(j = i+1; j < numsSize; j++)
		{
			if(nums[i] + nums[j] == target)
			{
				ret[0] = i;
				ret[1] = j;
				return ret;
			}
		}
	}
}
