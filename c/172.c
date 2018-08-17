#include <stdio.h>

int trailingZeroes(int n) {
	if(n < 1)
		return 0;

	int cnt_five = 0;
	while(n)
	{
		cnt_five += n / 5;
		n = n /5;
	}
	return cnt_five;
}
