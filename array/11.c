#include "array.h"

//version 2 
//based on that  if(a < b)
//				 then a*b <= (a+1)*(b-1)
//				 so we can use line 12
int maxArea(int* height, int heightSize) {
	int left=0, right=heightSize-1;
	int max = 0;
	while(left < right)
	{
		int area = (right-left)*(height[left] < height[right]? height[left++] : height[right--]);
		max = max > area? max : area;
	}
	return max;
}


//version1 time exceed
#define area(hei,len) (hei)*(len)
#define high(a,b) (a)>(b)?(b):(a)

int maxArea(int* height, int heightSize) {
	if(!height || heightSize <= 1)
		return 0;

	int left, right, varea;
	int max = 0;

	for(left = 0; left < heightSize-2; left++)
	{
		for(right = left+1; right < heightSize-1; right++)
		{
			varea = area((height[left], height[right]),(right-left));
			if(varea > max)
				max = varea;
		}
	}
	return max;
}

void main()
{
	int test[4] = {1,4,6,7};
	printf("%d\n", maxArea(test, 4));
}

