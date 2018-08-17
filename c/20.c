#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define bool int 
#define false 0
#define true  1


bool match(char a, char b)
{
	if((a == '{' && b == '}') || (a == '[' && b == ']') || (a == '(' && b == ')'))
		return true;
	else
		return false;
}

bool isValid(char* s) {
	if(s == NULL || s[0] == '\0')
		return true;

	int len = strlen(s);
	char *t = malloc(sizeof(char)*len);    
	if(len % 2)
		return false;
	else
	{
		t[0] = s[0];
		for(int i = 1,j = 1; i < len; i++)
		{
			t[j] = s[i];
			if(match(t[j-1], t[j]))
			{
				t[--j] = '\0';      
			}
			else
				j++;
		}
		if(t[0] == '\0')
			return true;
		else
			return false;
	}
}
void main()
{
	char *a = "{}()[[]([()])]";
	printf("%d\n", isValid(a));
	return ;
}
