class Solution:
    """
    0   1   2   3   4   5
    ----------------------
    7   1   5   3   6   4
    """
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        if n == 0: return 0
        last_zero = n-1
        while prices[last_zero] == 0:
            last_zero -= 1
        
        prices = prices[:last_zero+1]
        n = len(prices)
        
        """
        dp[i, j] represents the max price we buy the last item on i'th day
        and sell it on j'th
        """
        dp = [0 for i in range(n)]
        dp[n-1] = 0
        dp[n-2] = max(self.profit(prices, n-2, n-1), 0)
        
        for i in range(n-3, -1, -1):
            profits_at_i = (
                self.profit(prices, i, j)+dp[j+1] for j in range(i+1, n-1)
            )
            
            # print(f"{i}: {profits_at_i}")
            max_at_i = max(profits_at_i) if profits_at_i else 0
            max_ = max(max_at_i, dp[i+1], self.profit(prices, i, n-1))
            
            dp[i] = max_
        
        # print(dp)
        return dp[0]
        
    def profit(self, prices, i, j):
        return prices[j] - prices[i]