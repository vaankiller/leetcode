#include "array.h"

int lengthOfLIS(int* nums, int numsSize) {
	int cnt = 1, max = 0;
	int piovt = 0;

	for(int i = 0; i < numsSize; i++)
	{
		cnt = 1;
		for(int j = i+1,piovt = nums[j-1]; j < numsSize; j++)
		{
			;
			if(nums[j] > piovt)
			{
				cnt++;
				piovt = nums[j];
				printf("%d, %d\n", cnt, piovt);
			}
		}
		if(cnt > max)
			max = cnt;
	}
	return max;
}


void main()
{
	int test[9] = {10,9,2,5,3,4};
	int ret = 0;

	ret = lengthOfLIS(test, 6);
	printf("%d\n", ret);

	return;
}
