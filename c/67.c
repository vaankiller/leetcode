#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char* addBinary(char* a, char* b) {
	
	
	


}
//version 2: it works, but test case will be overflow... shit,go back to alpha...
char* addBinary(char* a, char* b) {
	int len_a = strlen(a);
	int len_b = strlen(b);
	int i_a = 0, i_b = 0, sum = 0; 
	for(int i = len_a-1; i >= 0 ; i--)
		i_a += (a[i]-48)<<(len_a-1-i);
	for(int i = len_b-1; i >= 0; i--)
		i_b += (b[i]-48)<<(len_b-1-i);
	sum = i_a + i_b;

	char* ret = malloc(sizeof(char) * 33);
	for(int i = 31; i > 0; i--)
	{
		if((sum&(1<<(31-i)))>>(31-i))
			ret[i] = '1';
		else
			ret[i] = '0';
	}
	for(int i = 0; i < 32; i++)
	{
		if(ret[i] == '1')
			return ret+i;
	}
	ret[0] = '0'; ret[1] = '\0';
	return ret;
}


void main()
{
	char *a = "0";
	char *b = "1";
	char *c = NULL;
	c = addBinary(a, b);
	puts(c);
	return ;
}
// version 1 , use char to judge, too fucking boring and hard
/*
char* addBinary(char* a, char* b) {
	int len_a = strlen(a); int len_b = strlen(b);
	int len_ret = len_a>len_b?len_a:len_b + 1;

	char *ret = malloc(sizeof(char)*(len_ret));
	bool c = 0;
	for(int i = len_ret-1; len_a>= 0 && len_b >= 0; i--)
	{
		if(a[len_a-1] == b[len_b-1])
		{
			if(c == 1)
				ret[i] = '1';
			else
				ret[i] = '0';

			if(a[len_a-1] == 1)
				c = 1;
			else
				c = 0;
		}
		if(a[len_a-1] != b[len_b-1])
		{
			if(c == 1)
			{
				ret[i] = '0';
				c = 1;
			}
			else
			{
				ret[i] = '1';
				c = 0;
			}
		}
		len_a--; len_b--;
	}
	if(c != 1)
		return ;
	else
		ret[0] = '1';
	return ret
}
*/
