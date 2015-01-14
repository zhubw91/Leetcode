class Solution:
	# @param num, a list of integer
	# @return a list of lists of integer	
	def subsetsWithDup(self,S):
		result = [[]]
		last = None
		dup = 0
		S.sort()
		for num in S:
			temp = result[:]
			if num == last:
				dup += 1
			else:
				dup = 0
			for i in temp:
				#print result
				if num == last:
					if len(i) >= dup and i[len(i)-dup:len(i)] == [num]*dup:
						#print i
						j = i[:]
						j.append(num)
						result.append(j)
				else:
					if len(i) == 0 or i[-1] < num:
						j = i[:]
						j.append(num)
						result.append(j)
			last = num
		return result
        		