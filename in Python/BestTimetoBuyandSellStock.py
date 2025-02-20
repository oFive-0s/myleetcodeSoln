class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #initialize variables for the minimum price and max profit
        min_price = float('inf')
        max_profit = 0
        
        #loop through each price in the list
        for price in prices:
            #update the minimum price if the current price is lower
            if price < min_price:
                min_price = price
            #calculate the profit if selling at current price
            profit = price - min_price
            #update the maximum profit if the current profit is higher
            if profit > max_profit:
                max_profit = profit
        
        return max_profit

#example usage
solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
print(solution.maxProfit([7, 6, 4, 3, 1]))     # Output: 0
