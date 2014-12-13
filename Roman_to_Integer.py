def romanToInt(s):
	roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
	last = 2000
	result = 0
	for letter in s:
		if roman.get(letter) > last:
			result += roman.get(letter) - 2*last
		else:
			result += roman.get(letter)
		last = roman.get(letter)

	return result

print romanToInt('MCMXCVIII')

