/*121. Best Time to Buy and Sell Stock
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
0 <= prices[i] <= 104 */


class best_time_to_buy_and_sell_stock {
    public int maxProfit(int[] prices) {
        if (prices.length < 2) return 0;
        int max_diff = 0;
        int cheapest_so_far = prices[0];

        for (int i = 1; i < prices.length; i++){
            if (prices[i] < cheapest_so_far) {cheapest_so_far = prices[i]; continue;}
            if (prices[i] - cheapest_so_far > max_diff) max_diff = prices[i] - cheapest_so_far;
        }
        return max_diff;
    }

    public static void main(String[] args) {
        int[] prices1 = {7, 1, 5, 3, 6, 4};
        int[] prices2 = {7, 6, 4, 3, 1};
        best_time_to_buy_and_sell_stock obj = new best_time_to_buy_and_sell_stock();
        System.out.println(obj.maxProfit(prices1));
        System.out.println(obj.maxProfit(prices2));
    }
}
