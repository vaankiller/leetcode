#include <stdio.h>
#define true 1
#define false 0
#define bool int

bool isUgly(int num) {
	if(num <= 0)
		return false;
	else if(num == 1)
		return true;
	else
	{
		while(num % 2 == 0)
			num /= 2;
		while(num % 3 == 0)
			num /= 3;
		while(num % 5 == 0)
			num /= 5;
	}
	return num==1?true:false;    
}

void main()
{
	printf("2 : %d\n", isUgly(2));
	printf("3 : %d\n", isUgly(3));
	printf("5 : %d\n", isUgly(5));
	printf("7 : %d\n", isUgly(7));
	printf("30 : %d\n", isUgly(30));
}
