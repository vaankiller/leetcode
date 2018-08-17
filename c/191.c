

int hammingWeight(uint32_t n) {
	int i = 0;
	while(n)
	{

		n &= n-1;
		i++;
	}   
	return i;
}
