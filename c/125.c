#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define bool int
#define true 1
#define false 0

bool isPalindrome(char* s) 
{

}

void main()
{
	char *s = "wow"
	printf("ret : %d\n", isPalindrome(s));

	return ;
}

//version 1: time limited 
/*
bool isPalindrome(char* s) {
	if(!s)
		return true;

	int len = strlen(s); 
	int cnt = -1;
	char *meta = malloc(sizeof(char)*(len));

	for(int i = 0; i < len; i++)
	{
		if(isalpha(s[i]) != 0)
		{
			putchar(s[i]);
			meta[++cnt] = tolower(s[i]);
		}
	}
	
	int i = 0;
	while( i < cnt)    
	{
		if(meta[i] == meta[cnt])
		{
			i++;
			cnt--;
		}
		else
			return false;
	}
	return true;
}
*/
