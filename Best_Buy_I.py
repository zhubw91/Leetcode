class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) is 0:
        	return 0
        minprice = prices[0]
        profit = 0
        for item in prices:
        	if item < minprice:
        		minprice = item
        	if item - minprice > profit:
        		profit = item - minprice
        return profit
