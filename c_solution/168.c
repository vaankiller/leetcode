
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* convertToTitle(int n) {
	if(n <= 0)
		return NULL;

	char *ret = malloc(sizeof(char)*10);
	int i = 0;
	int q, m;

	q = n / 26;
	if(q > 26)
		q 

	m = n % 26;
	
	
	return ret+i;
}
void main()
{
	int i = 0;

	for(i = 1; i < 54; i++)
		printf("%d : %s\n", i, convertToTitle(i));
	return;
}
//version 1 recursive 
/*
char* convertToTitle(int n) {
	if(n <= 0)
		return NULL;

	char *ret = malloc(sizeof(char)*10);
	int i = 0;

	while(n/26+1)
	{
		ret[i] = *convertToTitle(n/26+1);
		i++;
		n -= (ret[i-1] - 'A' + 1) * 26;
	}
	ret[i] = n - 1 + 'A';
	return ret; 
}
*/
