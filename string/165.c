#include <string.h>
#include "mystr.h"

int compareVersion(char* version1, char* version2)
{
	char* rest1 =NULL;
	char* rest2 =NULL;
	char *token1 = strtok_r(version1, ".", &rest1);
	char *token2 = strtok_r(version2, ".", &rest2);
	int result = 0;

	while(token1 != NULL | token2 != NULL)
	{
		result = compareToken(token1, token2);
		if (result != 0)
			return result;
		else
		{
			token1 = strtok_r(rest1, ".", &rest1);
			token2 = strtok_r(rest2, ".", &rest2);
		}
	}
	return result;
}

int compareToken(char* token1, char* token2)
{
	token1 = token1 == NULL ? "0": token1;
	token2 = token2 == NULL ? "0": token2;
	int result = -2;

	if(atoi(token1) > atoi(token2))
		result = 1;
	else if(atoi(token1) < atoi(token2))
		result = -1;
	else
		result = 0;
	return result;					
}
//version 2 ... 
int compareVersion(char* version1, char* version2)
{
	int len1 = strlen(version1);
	int len2 = strlen(version2);
	char *c1 = malloc(sizeof(char)*len1+1);
	char *c2 = malloc(sizeof(char)*len2+1);
	char *p1,*p2;
	int cnt1 = 1, cnt2 = 1, i = 0, j = 0;

	strcpy(c1, version1); strcpy(c2, version2);
	for(i = 0; i < len1; i++)
		if(c1[i] == '.') cnt1++;
	for(i = 0; i < len1; i++)
		if(c2[i] == '.') cnt2++;

	int *i1 = malloc(sizeof(int)*cnt1);
	int *i2 = malloc(sizeof(int)*cnt2);

	if(cnt1 == 1) i1[0] = atoi(c1);
	else
	{
		p1 = strtok(c1, "."); i1[0] = atoi(p1);
		while(p1 = strtok(NULL, ".")) i1[++j] = atoi(p1);
	}

	j = 0;
	if(cnt2 == 1) i2[0] = atoi(c2);
	else
	{
		p2 = strtok(c2, "."); i2[0] = atoi(p2);
		while(p2 = strtok(NULL, ".")) i2[++j] = atoi(p2);
	}
	for(i = 0; i < cnt1 && i < cnt2; i++)
	{
		if(i1[i] > i2[i]) return 1;
		else if(i1[i] < i2[i]) return -1;
	}
	if(cnt1 > cnt2) 
		for(; i < cnt1; i++) if(i1[i] > 0) return 1;
	else if(cnt1 < cnt2)
		for(; i < cnt2; i++) if(i2[i] > 0) return -1;
	else return 0;
}

void main()
{
	char *a = "19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0000.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000";
	char *b = "19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0000.0.0.0.0";
	printf("ret : %d\n", compareVersion(a, b));
	return;
}




//version 1
/*
int compareVersion(char* version1, char* version2)
{
	if(!version1 || !version2)
		return 0;

	int len1 = strlen(version1);
	int len2 = strlen(version2);
	int point1 = 0,  point2 = 0;
	int main1 = 0, main2 = 0;
	int dec1 = 0, dec2 = 0;
	char *c1 = malloc(sizeof(char)*len1+1);
	char *c2 = malloc(sizeof(char)*len2+1);

	c1[len1] = 0; c2[len2] = 0;
	strcpy(c1, version1); strcpy(c2, version2);

	for(int i = 0; i < len1; i++)
		if(version1[i] == '.') point1 = i;
	for(int i = 0; i < len2; i++)
		if(version2[i] == '.') point2 = i;

	if(point1) c1[point1] = '\0';
	if(point2) c2[point2] = '\0';

	main1 = atoi(version1);
	main2 = atoi(version2);

	if(main1 > main2)
		return 1;
	else if(main1 < main2)
		return -1;
	else if (main1 == main2)
	{
		if(point1 == 0 && point2 == 0)
			return 0;
		else if(point1 != 0 && point2 == 0)
			return 1;
		else if(point1 == 0 && point2 != 0)
			return -1;
		else
		{
			dec1 = atoi(version1 + point1 + 1);		
			dec2 = atoi(version2 + point2 + 1);
			return dec1==dec2?0:(dec1>dec2?1:-1);
		}
	}
}
*/
