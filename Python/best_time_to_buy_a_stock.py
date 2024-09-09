"""121. Best Time to Buy and Sell Stock
Easy
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104"""

import pytest
from typing import List

class Solution:
    
    def test(self):
        return self.maxProfit([1, 2, 3, 4, 5, 6, 8] )# list(range(1, 10000))[::-1] + [0]*10000)
    
    def maxProfit(self, prices: List[int]) -> int:
        """
            Calculate the maximum profit from buying and selling a stock given a list of prices.

            This function evaluates the prices of a stock over time and determines the best possible profit 
            that can be achieved by buying at a low price and selling at a higher price later. If no profit 
            can be made, it returns zero.

            Args:
                prices (List[int]): A list of integers representing the stock prices on different days.

            Returns:
                int: The maximum profit that can be achieved. Returns 0 if no profit is possible.

            Raises:
                ValueError: If prices is not a list of integers.
        """
        
        # exit early if no profit can be obtained
        if not prices or len(prices) == 1:
            return 0
        
        # the cheapest price seen is the first element in the list, max profit is 0
        cheapest_so_far, max_profit = prices[0], 0
        
        # check each price, if it is cheaper than anything we have seen, update the window. 
        #   If the current window gives a better profit than anything before it, update the max profit
        for p in prices:
            if p < cheapest_so_far:
                cheapest_so_far = p
            elif p - cheapest_so_far > max_profit:
                max_profit = p- cheapest_so_far
        
        # return the max profit
        return max_profit

@pytest.mark.parametrize(
    "prices, expected",
    [
        # Happy path tests
        ([7, 1, 5, 3, 6, 4], 5),  # ID: profit_possible
        ([7, 6, 4, 3, 1], 0),     # ID: no_profit_possible
        ([1, 2, 3, 4, 5], 4),     # ID: increasing_prices

        # Edge cases
        ([], 0),                  # ID: empty_list
        ([1], 0),                 # ID: single_element
        ([2, 4, 1], 2),           # ID: small_list

        # Error cases
        ([1, -1, 2], 3),          # ID: negative_prices
    ],
    ids = [
        "profit_possible", "no_profit_possible", "increasing_prices", 
        "empty_list", "single_element", "small_list", "negative_prices"
    ]
)
def test_maxProfit(prices, expected):
    # Act
    result = Solution().maxProfit(prices)

    # Assert
    assert result == expected

if __name__ == "__main__":
    print(Solution().test())