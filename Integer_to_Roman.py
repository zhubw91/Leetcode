class Solution:
    # @return a string
    def intToRoman(self, num):
        roman_dict = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),(100, 'C'), \
        (90, 'XC'), (50, 'L'), (40, 'XL'),(10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        for kv in roman_dict:
        	if kv[0] <= num:
        		return kv[1] + self.intToRoman(num-kv[0])
        return ''
