#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int** generate(int numRows, int** columnSizes) {
	if(numRows == 0)
		return 0;
	int **ret = (int**)calloc(sizeof(int), numRows*numRows);
	*columnSizes = (int*)malloc(sizeof(int) * numRows);
	int i,j;
	for(i = 0; i < numRows; i++)
	{
		ret[i] = (int*)malloc(sizeof(int)*numRows);
		ret[i][0] = 1; columnSizes[i][0] = i+1;
	}
	for(i = 1; i < numRows; i++)
	{
		for(j = 1; j < i+1; j++)
		{
			ret[i][j] = ret[i-1][j] + ret[i-1][j-1];
		}
	}
	return ret;
}

void main()
{
	int **b = malloc(sizeof(int)*5);
	generate(5,b);
	return;
}
