

int lengthOfLastWord(char* s) {
	if(s == NULL)  
		return 0;
	int cnt = 0;
	int flag = s[0]==' '?0:1;
	for(int i = 0; i < strlen(s); i++)
	{
		if(s[i] != ' ')
		{
			if(flag == 0)
			{
				cnt = 0;
				flag = 1;
			}
			cnt++;
		}
		else
			flag = 0;
	}
	return cnt;
}
