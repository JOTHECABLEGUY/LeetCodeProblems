/*122. Best Time to Buy and Sell Stock II
Medium
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.


Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104 */

class Solution {

    /**
     * Method to calculate the maximum profit of trading stocks given a list of their prices 
     *  organized by time. Stocks can be sold and bought on the same day, and multiple trades
     *  can be made throughout the course of the traversal. Can only hold 1 stock at a time
     * @param prices (int[]): list of prices for the stock sorted by time
     * @return int: maximum profit obtainable trading under the above conditions
     */
    public int maxProfit(int[] prices) {

        // return early if no profit available
        if (prices.length < 2) return 0;

        // max profit is set to 0 since no trades have been made
        int maxProfit = 0;

        // traverse the array for possible sell points
        for (int sell = 1; sell < prices.length; sell++){

            // if the stock ever rises above the buy price, sell for profit
            if (prices[sell] > prices[sell-1]) maxProfit += prices[sell] - prices[sell-1];
        }

        // return max profit
        return maxProfit;
    }

    public static void main(String[] args) {
        Solution obj = new Solution();
        int[] prices = new int[]{7,1,5,3,6,4};
        System.out.println(obj.maxProfit(prices));
    }
}
