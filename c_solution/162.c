#include "array.h"

int findPeakElement(int* nums, int numsSize) {
	int idx = (numsSize-1)/2;

	while(idx >= 0 && idx <= numsSize-1)
	{
		if(nums[idx] > nums[idx+1] && nums[idx] > nums[idx-1])
			return idx;
		else
		{
			 findPeakElement(nums, idx)
				findPeakElement(nums+idx+1, numsSize-idx-1);
		}
	}
}


void main()
{
	int test[1] = {-2147483648};

	printf("%d\n", findPeakElement(test, 1));

	return ;
}
