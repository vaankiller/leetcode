#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int romanToInt(char* s) {
	if(*s == 0)
		return 0;
	int sum,i,j,alpha;
	int* vector = malloc(sizeof(char) * strlen(s));
	for(i = 0; i < strlen(s); i++)
	{
		switch(s[i])
		{
			case 'I':
				vector[i] = 1; break;
			case 'V':
				vector[i] = 5; break;
			case 'X':
				vector[i] = 10; break;
			case 'L':
				vector[i] = 50; break;
			case 'C':
				vector[i] = 100; break;
			case 'D':
				vector[i] = 500; break;
			case 'M':
				vector[i] = 1000; break;
		}
	}
	for(i = 0; i < strlen(s); i++)
	{
		for(j = 1; j < 4 && i+j <= strlen(s); j++)
		{
			if(vector[i] < vector[i+j])
			{
				vector[i+j] -= vector[i] * j;
				i += j;
				break;
			}
		}
		sum += vector[i];
	}
	return sum;
}


void main()
{
	char *a = "MDCCCLXXXIV";
	printf("%d\n", romanToInt(a));
}
