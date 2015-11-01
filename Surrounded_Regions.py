class Solution(object):
	def solve(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		m = len(board)
		if m == 0:
			return
		n = len(board[0])
		visited = {}
		for i in range(m):
			for j in range(n):
				if board[i][j] == 'X' or (i,j) in visited:
					continue
				q = [(i,j)]
				head = 0
				tail = 1
				if_surrounded = 1
				visited[(i,j)] = 1
				while head < tail:
					x,y = q[head]
					if x in [0,m-1] or y in [0,n-1]:
						if_surrounded = 0
					if x > 0 and (x-1,y) not in visited and board[x-1][y] == 'O':
						visited[(x-1,y)] = 1
						q.append((x-1,y))
						tail += 1
					if x < m-1 and (x+1,y) not in visited and board[x+1][y] == 'O':
						visited[(x+1,y)] = 1
						q.append((x+1,y))
						tail += 1
					if y > 0 and (x,y-1) not in visited and board[x][y-1] == 'O':
						visited[(x,y-1)] = 1
						q.append((x,y-1))
						tail += 1
					if y < n-1 and (x,y+1) not in visited and board[x][y+1] == 'O':
						visited[(x,y+1)] = 1
						q.append((x,y+1))
						tail += 1
					head += 1
				if if_surrounded == 1:
					for node in q:
						board[node[0]][node[1]] = 'X'