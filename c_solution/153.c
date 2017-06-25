#include "array.h"


int vfindMin(int* nums, int start, int end)
{
	if(nums[start] < nums[end])
		return nums[start];
	else 
	{
		if(nums[(end-start)/2 + start] > nums[end])
			return vfindMin(nums, (end-start)/2+start+1, end);
		else if(nums[(end-start)/2 + start] < nums[end])
			return vfindMin(nums, start, start+(end-start)/2);
	}
}

int findMin(int* nums, int numsSize) 
{
	if(!nums)
		return NULL;

	return vfindMin(nums, 0, numsSize-1);
}
