#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int removeDuplicates(int* nums, int numsSize) {
	if(!numsSize)
		return 0;

	int index = 0;
	for(int i = 0; i < numsSize - 1; i++)
		if(nums[i] != nums[i+1]) 
			nums[index++] = nums[i];

	nums[index++] = nums[numsSize - 1];
	return index;
}
