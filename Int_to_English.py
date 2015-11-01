class Solution(object):
	def __init__(self):
		self.s1 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine", \
					"Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
		self.s2 = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
		self.s3 = ["","Thousand","Million","Billion"]
	def parse(self,num):
		t = num/100
		num = num % 100
		result = ""
		if t>0:
			result += self.s1[t] + " " + "Hundred"
		if num >= 20:
			t = num/10
			result += " " + self.s2[t]
			if num%10 > 0:
				result += " " + self.s1[num%10]
		elif num > 0:
			result += " " + self.s1[num]
		if len(result)>0 and result[0] == " ":
			result = result[1:]
		return result

	def numberToWords(self, num):
		"""
		:type num: int
		:rtype: str
		"""
		result = ""
		t = 0
		while num > 0:
			tmp = self.parse(num%1000)
			if t == 0:
				result = tmp
			elif tmp != "":
				if result == "":
					result = tmp + " " + self.s3[t]
				else:
					result = tmp + " " + self.s3[t] + " " + result
			t += 1
			num = num/1000
		if result == "":
			return "Zero"
		return result
