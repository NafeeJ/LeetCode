class Solution: 
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0:0}
        res = self.getMin(coins, amount, memo)
        
        if res == float('inf'):
            return -1
        
        return res
        
    def getMin(self, coins: List[int], amount: int, memo={}) -> int:
        if amount in memo:
            return memo[amount]
        
        min_coins = float('inf')
        for c in coins:
            if amount >= 0:
                num_coins = self.getMin(coins, amount - c, memo)
                if num_coins != -1:
                    min_coins = min(min_coins, num_coins + 1)
        
        memo[amount] = min_coins
        return min_coins