# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        prices: price of stock ith day
        
        Approach: 
        Two pointer and sliding window
        Move r to the right to evaluate the sell price and its profit
        Move l to the right only when price is too low causing loss

        Example:  
        prices = [7,1,5,3,6,4]
        l=0,r=0: buy 7 sell 7, profit = 0
        l=0,r=1: buy 7 sell 1? No => buy 1
        l=1,r=2: buy 1 sell 5, profit = 4
        l=1,r=3: buy 1 sell 3, profit = 2
        l=1,r=6: buy 1 sell 6, profit = 5 (*) max
        l=1,r=7: buy 1 sell 4, profit = 3

        return 5
        """
        if prices is None or len(prices) == 0:
            return 0
            
        l = 0
        max_profit= 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
                   
        return max_profit

    # The same algorithm with above, but two pointers are hidden
    def maxProfit_bak(self, prices: List[int]) -> int:
        """
        Maximize profit with the best decision when to buy and sell
        return max_profit

        Approach:
        Let's assume that I bought stock the day 1 and iterate the prices to simulate the profit. 
        If the price is lower than before, wrong decision in the past. That is the time to buy.
        If the price is higher than before, time to sell. Update the maximum profit.

        Example 1:
        prices = [7,1,5,3,6,4]

        Example 2:
        prices = [7,6,4,3,1]
        """
        
        if prices is None or len(prices) == 0:
            return 0

        max_profit = 0
        buy = prices[0]
        
        for price in prices:
            if buy > price: 
                buy = price
            else:
                max_profit = max(max_profit, price - buy) 

        return max_profit


