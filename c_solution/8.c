#include "mystr.h"

#define p printf
int mystr(char* str)
{
	if(!str)
		return 0;

	int len = strlen(str);
	int i, cnt == 0;, ret = 0;

	for(i = 0; i < len; i++)
	{
		if(isdigit(str[i]))
		{
			
		}
		else if(str[i] == ' ' && ret == 0)
			continue;
		else
			return ret;
	}
	return ret;
}

void main()
{
	int ret = 0;

	p("%d\n", mystr("123"));
	p("%d\n", mystr("-123"));
	p("%d\n", mystr("  123"));
	p("%d\n", mystr("1 2 3 "));
	p("%d\n", mystr("./123"));
	p("%d\n", mystr("1b2c3f"));
	p("%d\n", mystr(".das . aqe"));
}
