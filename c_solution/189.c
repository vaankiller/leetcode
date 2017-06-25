#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void main()
{
	int i = 0;
	int a[13] = {1,2,3,4,5,6,7,8,9,10,11,12,13};
	int b[6] = {1,2,3,4,5,6};
	rotate(a, 6, 3);
	for(i = 0; i < 6; i++)
		printf("%d ", a[i]);

	return ;
}


//version 3 fix the bug, but the problem is not even or odd,
//is numsSize = nk; that's the trick
/*
void rotate(int* nums, int numsSize, int k) {
	if(!nums || numsSize == 1 || k%numsSize == 0)
		return ;

	int tmp = nums[0];
	k %= numsSize;
	if(numsSize%2 == 0 && k%2 == 0)
	{
		for(int i = 0, j = 0; i < numsSize/2; i++)
		{
			nums[j] = nums[(j-k+numsSize)%numsSize];
			j = (j-k+numsSize)%numsSize;
		}
		nums[k%numsSize] = tmp;
		for(int i = 0; i < numsSize; i++)
			printf("%d ", nums[i]);
		puts("");
		tmp = nums[1];
		for(int i = 0, j = 1; i < numsSize/2; i++)
		{
			nums[j] = nums[(j-k+numsSize)%numsSize];
			j = (j-k+numsSize)%numsSize;
		}
		nums[(1+k)%numsSize] = tmp;
	}
	else
	{
		for(int i = 0, j = 0; i < numsSize; i++)
		{
			for(int i = 0; i < numsSize; i++)
				printf("%d ", nums[i]);
			puts("");
			nums[j] = nums[(j-k+numsSize)%numsSize];
			j = (j-k+numsSize)%numsSize;
		}
		nums[k%numsSize] = tmp;
		for(int i = 0; i < numsSize; i++)
			printf("%d ", nums[i]);
		puts("");
	}
	return;
}
*/

//version2 recursive ,,,time limited
/*
void rotate(int* nums, int numsSize, int k) {
	if(!nums || numsSize == 1 || k%numsSize == 0)
		return ;

	for(int i = 0; i < 13; i++)
		printf("%d ", nums[i]);
	puts("");
	k %= numsSize;
	int tmp = nums[numsSize-1];

	if(k == 0)
		return ;
	else
	{
		for(int i = numsSize-1; i > 0; i--)
			nums[i] = nums[i-1];
		nums[0] = tmp;
		rotate(nums, numsSize, k-1);
	}
	return ;
}
*/



//version 1, bug,  1 2 3 4 5, if k = 2, crash,,only odd can move
/*
void rotate(int* nums, int numsSize, int k) {
	if(!nums || numsSize == 1 || k%numsSize == 0)
		return ;

	int tmp = nums[0];
	k %= numsSize;

	for(int i = 0, j = 0; i < numsSize; i++)
	{
		for(int j = 0; j < numsSize; j++)
			printf("%d ", nums[j]);
		puts("");
		nums[j] = nums[(j-k+numsSize)%numsSize];
		j = (j-k+numsSize)%numsSize;
	}
	nums[k%numsSize] = tmp;
	return;
}
*/
