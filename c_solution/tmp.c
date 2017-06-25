#include "array.h"

void main()
{
	int** test = malloc(sizeof(int)*4*4);

	printf("%lu\n", sizeof(int*));
	printf("%p\n%p\n%p\n%p\n", test, test+1, test+2, test+3);

	int a = 6;
	int b = 11;
	test[0] = &a;
	test[3] = &b;
	*test[0] = 8;
	printf("%p\n", test[0]);
	printf("%p\n", &test[0][1]);
	printf("%p\n", &test[0][2]);
	printf("%p\n", &test[0][3]);
	printf("%p\n", &test[3][0]);
	printf("%d\n", test[3][0]);
	printf("%p\n", &b);

}
