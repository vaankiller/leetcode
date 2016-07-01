#include <stdio.h>
#include <stdlib.h>

void moveZeroes(int* nums, int numsSize);
void main()
{
	int a[] = {0,1,0,3,12};
	int k = 0;
	moveZeroes(a, 5);

	while(k < 5)
	{
		printf("%d,", a[k]); k++;
		printf("\n");
	}
}

void moveZeroes(int* nums, int numsSize) {
	if(nums == NULL || numsSize == 1)
		return;
	int cnt = 0; int i = 0, j = 0;

	for(i = 0; i < numsSize; i++)
		if(nums[i] == 0) cnt++;
	if(cnt == 0)
		return;
	else
	{
		for(i = 0; (i < numsSize) && (cnt > 0); i++)
		{
			if(nums[i] == 0)
			{
				cnt--; 
				for(j = i; j < numsSize-1; j++)
					nums[j] = nums[j+1];
				nums[j] = 0;
				i--;
			}                
		}
	}
	return ;
}
