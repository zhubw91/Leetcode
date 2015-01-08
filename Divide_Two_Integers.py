class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        op = 1
        a = dividend
        b = divisor
        if dividend < 0:
        	a = -a
        	op = -op
        if divisor < 0:
        	b = -b
        	op = -op
        tempb = b
        times = 0
        while a >= b:
        	t = 1
        	while a >= b:
        		b = b << 1
        		t = t << 1
        	b = b >> 1
        	t = t >> 1
        	a -= b
        	times += t
        	b = tempb
        if times > 2147483647 and op == 1:
        	times = 2147483647
        if times > 2147483648 and op == -1:
        	times = 2147483648
        return times if op == 1 else -times