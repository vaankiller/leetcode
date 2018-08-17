bool isPalindrome(int x) {
	int max = x;  
	int min = 0;  
	while(max >0){
		min *= 10;  
		min += max %10;  
		max /=10;  
	}  
	return min==x;  
}
