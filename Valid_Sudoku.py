class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        colhash = {}
        rowhash = {}
        matrixhash = {}
        for i,row in enumerate(board):
        	for j,num in enumerate(row):
        		if num != '.':
        			if colhash.has_key((j,num)) or rowhash.has_key((i,num)) or matrixhash.has_key((i/3*3+j/3+1,num)):
        				return False
        			colhash[(j,num)] = rowhash[(i,num)] = matrixhash[(i/3*3+j/3+1,num)] = 1
        return True