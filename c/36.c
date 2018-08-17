#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define bool int
#define true 1
#define false 0

bool isValidRow(char* board, int boardRowSize)
{
	char *nums = malloc(sizeof(char)*boardRowSize);
	for(int i = 0; i < boardRowSize; i++)
	{
		if(board[i] == '.')
			continue;
		else if(nums[atoi(&board[i])] == 0)
			nums[atoi(&board[i])] = 1;
		else
			return false;
	}
	return true;
}

bool isValidCol(char* board, int boardRowSize)
{
	char *nums = malloc(sizeof(char)*boardRowSize);
	for(int i = 0,j = 0; i < boardRowSize; i++, j += boardRowSize)
	{
		if(board[j] == '.')
			continue;
		else if(nums[atoi(&board[j])] == 0)
			nums[atoi(&board[j])] = 1;
		else
			return false;  
	}
	return true;
}

bool isValidSeq(char** board, int boardRowSize, int boardColSize, int row, int col)
{
	char *nums = malloc(sizeof(char)*boardRowSize);
	for(int i = row-1; i <= row+1; i++)
	{
		for(int j = col-1; j <= col+1; j++)
		{
			if(board[i][j] == '.')
				continue;
			else if(nums[atoi(&board[i][j])] == 0)
				nums[atoi(&board[i][j])] = 1;
			else
				return false;
		}
	}
	return true;
}
bool isValidSudoku(char** board, int boardRowSize, int boardColSize) 
{
	for(int i = 0; i < boardRowSize; i++)
	{
		if(!isValidRow(board[i], boardRowSize))
			return 0;
	}
	for(int i = 0; i < boardColSize; i++)
	{
		if(!isValidCol(&board[0][i], boardRowSize))
			return 0;
	}
	for(int i = 1, j = 1; i < 9 && j < 9; i+=2, j+=2)
	{
		if(!isValidSeq(board, boardRowSize, boardColSize, i, j))
			return 0;
	}
	return true;
}



void main()
{
	char m[9][9] = {".87654321","2........","3........","4........","5........","6........","7........","8........","9........"	};
	bool ret = -1;
	printf("ret : %d\n", isValidSudoku(m, 9, 9));
	return ;
}
