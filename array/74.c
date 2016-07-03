#include "array.h"

bool searchMatrix(int** matrix, int matrixRowSize, int matrixColSize, int target) {
	int max = 0;

	if(target < matrix[0][0] || target > matrix[matrixRowSize-1][matrixColSize-1])
		return false;

	for(int i = 0; i < matrixRowSize; i++)
	{
		if(target > matrix[i][matrixColSize-1])
			continue;
		else if(target == matrix[i][matrixColSize-1])
			return true;
		else
		{
			for(int j = 0; j < matrixColSize; j++)
			{
				if(target == matrix[i][j])
					return true;
			}
		}
	}
	return false;
}

void main()
{
	int test[2][2] = {1,1,3,3};

	printf("%d\n", searchMatrix(test, 2, 2, 2));
}





