class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board == None:
        	return None
        m = len(board)
        if m == 0:
        	return None
        n = len(board[0])
        for i in range(m):
        	for j in range(n):
        		cnt = 0
        		for x in range(max(0,i-1),min(i+2,m)):
        			for y in range(max(0,j-1),min(j+2,n)):
        				if (x,y) == (i,j):
        					continue
        				if board[x][y]%10 == 1:
        					cnt += 1
        		if board[i][j] == 1:
        			if cnt < 2 or cnt > 3:
        				board[i][j] = 11
        			else:
        				board[i][j] = 21
        		else:
        			if cnt == 3:
        				board[i][j] = 20
        			else:
        				board[i][j] = 10
        for i in range(m):
        	for j in range(n):
        		board[i][j] = board[i][j]/10 - 1
