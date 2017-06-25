#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void merge(int* nums1, int m, int* nums2, int n) {
	int pos1 = 0, pos2 = 0;
	if(!nums1 && !nums2)
		return;
	else if(nums2 == NULL || n == 0)
		return;
	else
	{
		int *ret = malloc(sizeof(int)*(m+n));
		for(int i = 0; pos1 < m && pos2 < n; i++)
		{
			if(nums1[pos1] < nums2[pos2])
				ret[i] = nums1[pos1++];
			else
				ret[i] = nums2[pos2++];
		}
		if(pos1 == m)
			for(int i = m+pos2; i < m+n; i++)
				ret[i] = nums2[pos2++];
		else if(pos2 == n)
			for(int i = n+pos1; i < m+n; i++)
				ret[i] = nums1[pos1++];
		for(int i = 0; i < m+n; i++)
			nums1[i] = ret[i];
	}
	return;
}


void main()
{

	int a[6] = {1,2,3,0,0,0};
	int b[3] = {2,5,6};

	merge(a,3,b,3);
	for(int i = 0; i < 6; i++)
		printf("%d,", a[i]);
	return;

}
