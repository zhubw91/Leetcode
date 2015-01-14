class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        colhash = {}
        rowhash = {}
        mhash = {}
        def isvalid(colhash, rowhash, mhash, board, x, y):
        	num = board[x][y]
        	if colhash.has_key((y,num)) or rowhash.has_key((x,num)) or mhash.has_key((x/3*3+y/3+1,num)):
        		return False
        	else:
        		updatehash(colhash, rowhash, mhash, board, x, y, 1)
        		return True
        # act = 0 remove act = 1 add
        def updatehash(colhash, rowhash, mhash, board, x, y, act):
        	num = board[x][y]
        	if act == 1:
        		colhash[(y,num)] = rowhash[(x,num)] = mhash[(x/3*3+y/3+1,num)] = 1
        	else:
        		del colhash[(y,num)]
        		del rowhash[(x,num)]
        		del mhash[(x/3*3+y/3+1,num)]
        def dfs(colhash, rowhash, mhash, board, pos):
        	x = pos/9
        	y = pos%9
        	if pos == 81:
        		return True
        	if board[x][y] != '.':
        		return dfs(colhash, rowhash, mhash, board, pos+1)
        	for i in range(1,10):
        		board[x][y] = str(i)
        		if isvalid(colhash, rowhash, mhash, board, x, y):
        		    if dfs(colhash, rowhash, mhash, board, pos+1):
        			    return True
        		    else:
        			    updatehash(colhash, rowhash, mhash, board, x, y, 0)
        		board[x][y] = '.'
        	return False
        for i in range(9):
        	for j in range(9):
        		if board[i][j] != '.':
        			updatehash(colhash, rowhash, mhash, board, i, j, 1)
        dfs(colhash, rowhash, mhash, board, 0)