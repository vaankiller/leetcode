#include <stdio.h>
#include <string.h>

void swap(int *a, int *b)
{

	int tmp = *a;
	*a = *b;
	*b = tmp;
}

int removeElement(int* nums, int numsSize, int val) {
	if(nums == NULL)
		return 0;
	int cnt = 0;
	int end = numsSize-1, i = 0;
	for(i = 0; i < numsSize; i++)
		if(nums[i] == val) cnt++;

	if(cnt == numsSize)
		return 0;
	for(i = 0; i < numsSize && cnt != 0; i++)
	{
		if(nums[i] == val) swap(&nums[i--], &nums[end--]);
		cnt--;
		printf("%d %d %d %d %d\n", nums[0], nums[1], nums[2], nums[3], nums[4]);
	}
	return end+1;
}



void main()
{
	int nums[5] = {3,1,3,3,3};
	printf("ret : %d\n", removeElement(nums, 5, 3));
}
