#include <stdio.h>
#include <string.h>
#define true 1
#define false 0
#define bool int

bool isHappy(int n) {
	puts("enter");
	if(n <= 0)
		return false;
	else if(n == 1)
		return true;
	int i = 0, m = 0, c= 0, j = 0;
	puts("before while");
	while(n)
	{
		puts("enter while");
		c = n % 10;
		n /= 10;
		for(j = 1; j < i+1; j++)
			j *= 10;
		m += (c * c) * j;
		i++;
	}
	printf("n : %d\n", m);
	return isHappy(m);
}

void main()
{
	int n = 1;
	printf("2 : %d\n", isHappy(2));
	/*
	for(n = 1; n < 11; n++)
	{
		printf("%d:%d\n", n, isHappy(n));
	}
	*/
}
