# 322. Coin Change (Medium)
# https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Minimum number of coins to make up the amount
        arg coins: a list of different denominations and infinite use possible
        return min_num_coins

        Approach: DP
        Sort coin denominations first
        Design and solve a smaller problem less than the given amount and memoize it
        Reuse it to solve bigger problems, the target amount

        Example 1:
        Possible combination
        coins = [1,2,5], amount = 11
        5 + 5 + 1 = 11
        return 3
        
        amount=1, memo=[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        amount=2, memo=[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        amount=3, memo=[0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0]
        amount=4, memo=[0, 1, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0]
        amount=5, memo=[0, 1, 1, 2, 2, 1, 0, 0, 0, 0, 0, 0]
        ...
        amount=10, memo=[0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 0]
        amount=11, memo=[0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]

        Example 2:
        Not possible with the denomination
        coins = [2], amount = 3
        return -1

        Example 3: No change_amount required
        coins = [1], amount = 0
        return 0
        """        
        coins.sort()
        amount_limit = amount +1
        memo = [0] * amount_limit

        # T=O(n * amount), S=O(n)
        for change_amount in range(1, amount_limit):
            min_num_coins = amount_limit # if denominated 1 max # of coins

            for denomination in coins:
                if change_amount < denomination:
                    break
                min_num_coins = min(min_num_coins, memo[change_amount - denomination] + 1)
            
            memo[change_amount] = min_num_coins
            #print (f"{change_amount}, memo={memo}")

        if memo[amount] < amount_limit:
            return memo[amount]
        else:
            return -1

