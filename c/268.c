#include "array.h"

int missingNumber(int* nums, int numsSize) {
	int *ret = malloc(sizeof(int)*numsSize);

	for(int i = 0; i < numsSize; i++)
		ret[i] = -1;
	for(int i = 0; i < numsSize; i++)
	{
		ret[nums[i]] = nums[i];
	}

	for(int i = 0; i < numsSize; i++)
	{
		if(ret[i] == -1)
			return i;
	}
}
