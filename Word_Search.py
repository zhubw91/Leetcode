class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        q = []
        head = 0
        tail = 1
        m = len(board)
        n = len(board[0])
        for i in range(m):
        	for j in range(n):
        		if board[i][j] != word[0]:
        			continue
        		head = 0
        		q = [(i,j,board[i][j],0)]
        		tail = 1
        		pos_hash = {}
        		while head < tail 