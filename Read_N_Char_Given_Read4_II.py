# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
	def __init__(self):
		self.queue = []

	def read(self, buf, n):
		"""
		:type buf: Destination buffer (List[str])
		:type n: Maximum number of characters to read (int)
		:rtype: The number of characters read (int)
		"""
		cnt = 0
		while True:
			temp = [""]*4
			num = read4(temp)
			self.queue.extend(temp)
			current_cnt = min(len(self.queue),n-cnt)
			for i in range(current_cnt):
				buf[cnt] = self.queue.pop(0)
				cnt += 1
			if current_cnt == 0:
				break
		return cnt


