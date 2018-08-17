class Solution(object):
	def numberOfArithmeticSlices(self, A):
		"""
		:type A: List[int]
		:rtype: int
		"""
		count = 0
		addend = 0
		for i in range(2, len(A)):
			if A[i]-A[i-1] == A[i-1]-A[i-2]:
				addend += 1
				count += addend
			else:
				addend = 0
		return count
																								            
