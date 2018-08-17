
int titleToNumber(char* s) {
	if(s == NULL)
		return 0;

	int len = strlen(s);
	int sum = 0, i = 0, j = 0;
	int alpha_num = 1;

	for(i = 0; i < len; i++)
	{
		alpha_num = s[i] - 'A' + 1;
		for(j = len-1; j > i; j--)
			alpha_num *= 26;
		sum += alpha_num;
	}
	return sum;
}
