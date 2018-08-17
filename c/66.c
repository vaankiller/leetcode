#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int* plusOne(int* digits, int digitsSize, int* returnSize) {
	int carry = 1, i = digitsSize;
	int* ret = (int*)malloc(sizeof(int)*(digitsSize+1));
	while (i > 0) {
		ret[i] = (digits[i-1]+carry)%10;
		printf("%d,", ret[i]);
		carry = (digits[i-1]+carry)/10;
		i--;
	}
	if (ret[1] == 0) {
		ret[0] = 1;
		*returnSize = digitsSize+1;
		return ret;
	} else {
		*returnSize = digitsSize;
		return ret+1;
	}
}

void main()
{
	int a[10] = {9,8,7,6,5,4,3,2,1,0};
	int s = 0;
	int *b = &s;
	int *ret = NULL;
	ret = plusOne(a, 10, b);
	for(s = 0; s < 10; s)
}
