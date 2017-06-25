#include "array.h"

bool searchMatrix(int** matrix, int matrixRowSize, int matrixColSize, int target) {
	int i = 0;
	int j = matrixColSize-1;

	while(i <= matrixRowSize-1 && j >= 0)
	{
		if(target > matrix[i][j])
			i++;
		else if(target == matrix[i][j])
			return true;
		else
			j--;
	}
	return false;
}
