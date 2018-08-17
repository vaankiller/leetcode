

#include <stdio.h>

int rob(int* nums, int numsSize) {
	int pre = 0, cur = 0;
	for (int i = 0; i < numsSize; ++i) {

		int tmp = nums[i] + pre;
		pre = cur;
		cur = (tmp > pre ? tmp : pre);
	}
	return cur;
} 
