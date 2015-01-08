class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        # find the row
        start = 0
        end = len(matrix) - 1
        while start <= end:
        	mid = (start + end)/2
        	if matrix[mid][0] == target:
        		return True
        	elif matrix[mid][0] > target:
        		end = mid - 1
        	else:
        		start = mid + 1
        if end == -1:
        	return False
        i = end
        start = 0
        end = len(matrix[0]) - 1
        while start <= end:
        	mid = (start + end)/2
        	if matrix[i][mid] == target:
        		return True
        	elif matrix[i][mid] > target:
        		end = mid - 1
        	else:
        		start = mid + 1
        return False
