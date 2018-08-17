#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define uint32_t unsigned int
uint32_t reverseBits(uint32_t n) {
	int i, j, head, tail;
	for(i = 31, j = 0; i > j; i--,j++)
	{
		head = (n>>i)&1; tail = (n&(1<<j))>>j;
		printf("head:%d tail:%d %d", head, tail, n&(1<<j));
		printf("n : %#x\n", n);
		if(head == tail)
			continue;
		else
		{
			if(head == 0)
			{
				n += 1<<i;
				n -= 1<<j;
			}
			else if(head == 1)
			{
				n -= 1<<i;
				n += 1<<j;
			}
		}
	}
	return n;
}

int main()
{
	printf("%u\n", reverseBits((unsigned int)4294967295));
}
