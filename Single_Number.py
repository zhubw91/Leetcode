def singleNumber(A):
	for i in range(0,len(A)-1):
		A[i+1] = A[i] ^ A[i+1]
	if len(A) == 1:
		return A[0]
	return A[i+1]


A = [1]
print singleNumber(A)