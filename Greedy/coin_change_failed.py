# 322. Coin Change (Medium)
# https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Minimum number of coins to make up the amount
        return cnt_coins

        Approach: Greedy
        Works only when the the denominations can be multiplied like a Korean won
        coins = [10, 50, 100, 500, 1000]
        amount = 800
        500 * 1 +  100 * 3 = 800
        return 4

        # T=O(n), S=O(1)
        """
        if not coins:
            return -1

        coins.sort(reverse=True)

        cnt_coins = 0
        
        for coin in coins:
            while coin <= amount and amount > 0:
                amount -= coin
                cnt_coins += 1
        
        return cnt_coins if amount == 0 else -1

# 51 / 189 testcases passed
# Failed case : coins = [186,419,83,408]
# To pass all test cases, use DP
# See also: ../DynamicProgramming/coin_change.py
