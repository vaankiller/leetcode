#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct NumArray {
	int* sums;
	int size;
};

/** Initialize your data structure here. */
struct NumArray* NumArrayCreate(int* nums, int numsSize) {
	struct NumArray* numArray = malloc(sizeof(struct NumArray));
	numArray->size = numsSize;
	numArray->sums = malloc(sizeof(int)*numsSize);
	numArray->sums[0] = nums[0];
	for(int i = 1; i < numsSize; i++)
	{
		numArray->sums[i] = numArray->sums[i-1] + nums[i]; 
	}

	return numArray;
}

int sumRange(struct NumArray* numArray, int i, int j) {
	if(!numArray)
		return 0;

	if(i == 0)
		return numArray->sums[j];
	else
		return numArray->sums[j] - numArray->sums[i-1];
}

/** Deallocates memory previously allocated for the data structure. */
void NumArrayFree(struct NumArray* numArray) {
	if(!numArray)
		return ;
	free(numArray->sums);
	free(numArray);

	return ;
}
