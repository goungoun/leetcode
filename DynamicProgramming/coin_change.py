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
        
        amount=1, memo=[0, 1]
        amount=2, memo=[0, 1, 1]
        amount=3, memo=[0, 1, 1, 2]
        amount=4, memo=[0, 1, 1, 2, 2]
        amount=5, memo=[0, 1, 1, 2, 2, 1]
        ...
        amount=10, memo=[0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2]
        amount=11, memo=[0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]

        Example 2:
        Not possible with the denomination
        coins = [2], amount = 3
        return -1

        Example 3: No change_amount required
        coins = [1], amount = 0
        return 0
        """
        if not amount:
            return 0
        
        if not coins:
            return -1

        coins.sort()
        upper_limit = amount + 1
        memo = [upper_limit] * upper_limit
        memo[0] = 0

        # T=O(n * amount), S=O(n)
        for change in range(1, upper_limit):
            min_cnt = upper_limit
            for coin in coins:
                if change < coin:
                    break
                min_cnt = min(min_cnt, memo[change - coin] + 1)
            
            memo[change] = min_cnt
            #print (f"{change}: memo={memo[:change +1]}")

        if memo[amount] >= upper_limit:
            return -1

        return memo[amount]
