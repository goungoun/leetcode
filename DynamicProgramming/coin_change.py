# 322. Coin Change (Medium)
# https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Working hybrid between Greedy and DP to solve this coin change problem. 
        The time complexity and space complexity of the Greedy approach is much better though, 
        if I have to choose only one approach between Greedy and DP, definitely DP because Greedy approach does not work in most cases. 
        """
        if coins is None or amount is None or amount == 0:
            return 0

        coins.sort()

        greedy_mode = True
        for i in range(1,len(coins)):
            if coins[i]%coins[i-1] != 0:
                greedy_mode = False
        print (f"greedy_mode={greedy_mode}")

        if greedy_mode:
            # T=O(n), S=O(1)
            return self.coinChangeGreedy(coins, amount)
        else:
            # T=O(n * amount), S=O(n)
            return self.coinChangeDp(coins, amount)

    def coinChangeDp(self, coins: List[int], amount: int) -> int:
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

    def coinChangeGreedy(self, coins: List[int], amount: int) -> int:
        """
        Warning!!!
        Greedy works only when the the denominations can be multiplied like a Korean won
        coins = [10, 50, 100, 500, 1000]
        amount = 800
        500 * 1 +  100 * 3 = 800
        return 4
        """
        coins.sort(reverse=True)

        cnt = 0
        
        # T=O(n), S=O(1)
        for coin in coins:
            while coin <= amount and amount > 0:
                amount -= coin
                cnt += 1

        if amount > 0:
            return -1 
        
        return cnt

