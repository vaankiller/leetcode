#include "array.h"


void rotate(int** matrix, int matrixRowSize, int matrixColSize) 
{
	if(!matrix || matrixRowSize == 1)
		return ;

	int** ret = malloc(sizeof(int)*matrixRowSize*matrixColSize);
	for(int i = 0; i < matrixRowSize; i++)
	{
		for(int j = 0; j < matrixColSize; j++)
		{
			ret[j*matrixRowSize+matrixColSize-1-i] = &matrix[i*matrixRowSize+j];
		}
	}
	for(int i = 0; i < matrixRowSize; i++)
	{
		for(int j = 0; j < matrixColSize; j++)
		{
			matrix[i][j] = ret[i][j];       
		}
	}
	return ;
}

void main()
{
	int test[1][4] = {1,2,3,4};
	rotate(test, 2, 2);
}
