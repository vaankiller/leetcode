
bool isBadVersion(int version);

int firstBadVersion(int n) {
	if(n <= 0)
		return 0;

	for(int i = 1; i <= n; i++)
	{
		if(isBadVersion(i))
			return i;
	}
	return 0;
}
