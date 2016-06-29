#include "array.h"

int comp(const void*a,const void*b)
{
	return *(int*)a-*(int*)b;
}

int singleNumber(int* nums, int numsSize) {
	if(nums == NULL || numsSize <= 1)
		return nums[0];

	int i = 0;
	qsort(nums, numsSize, sizeof(int), comp);

	for(i = 0; i < numsSize-1; i++)
	{
		if(nums[i] != nums[i+1])
			return nums[i];
		else
			i++;
	}
	if(i == numsSize)
		return nums[numsSize-1];

}

void main()
{
	int ret[5] = {3,3,2,1,1};

	printf("%d\n", singleNumber(ret, 5));

}
