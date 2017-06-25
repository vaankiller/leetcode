#include "array.h"

struct NumArray {
	int* array;
	int* sum;
	int size;
};

/** Initialize your data structure here. */
struct NumArray* NumArrayCreate(int* nums, int numsSize) {
	struct NumArray* p = malloc(sizeof(struct NumArray));
	p->size = numsSize;
	p->array = nums;
	p->sum = malloc(sizeof(int)*numsSize);

	p->sum[0] = nums[0];
	for(int i = 1; i < numsSize; i++)
	{
		p->sum[i] += p->sum[i-1] + p->array[i];
	}

	return p;
}

void update(struct NumArray* numArray, int i, int val) {
	numArray->array[i] = val;

	for(; i < numArray->size; i++)
	{
		numArray->sum[i] += val;
	}

	return ;
}

int sumRange(struct NumArray* numArray, int i, int j) {
	return numArray->sum[j] - numArray->sum[i] + numArray->array[i];
}

/** Deallocates memory previously allocated for the data structure. */
void NumArrayFree(struct NumArray* numArray) {
	free(numArray);
	numArray = NULL;
	return ;
}


void main()
{
	int test[3] = {0};
	struct NumArray* numArray = NumArrayCreate(test, 3);

	sumRange(numArray, 0, 1);
	update(numArray, 1, 10);
	sumRange(numArray, 1, 2);
	NumArrayFree(numArray);

	return ;
}
