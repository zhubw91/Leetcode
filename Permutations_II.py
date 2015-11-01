class Solution(object):
	def dfs(self,k,stack,visited,nums,result):
		if k == len(nums):
			result.append(stack[:])
		else:
			for i in range(len(nums)):
				if i > 0 and nums[i] == nums[i-1]:
					continue
				if visited[nums[i]] == 0:
					continue
				visited[nums[i]] -= 1
				stack[k] = nums[i]
				self.dfs(k+1,stack,visited,nums,result)
				visited[nums[i]] += 1


		
	def permuteUnique(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		result = []
		stack = [0] * len(nums)
		visited = {}
		for x in nums:
			if x not in visited:
				visited[x] = 0
			visited[x] += 1
		nums.sort()
		self.dfs(0,stack,visited,nums,result)
		return result

solution = Solution()
print solution.permuteUnique([-1,2,-1,2,1,-1,2,1])