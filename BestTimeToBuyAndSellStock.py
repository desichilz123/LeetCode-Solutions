class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0

        left_pointer = 0
        right_pointer = 1

        while (left_pointer < len(prices) - 1 and right_pointer < len(prices)):
            if (prices[left_pointer] > prices[right_pointer]):
                left_pointer += 1
                right_pointer = left_pointer + 1
            else:
                max_profit = max(max_profit, prices[right_pointer] - prices[left_pointer])
                right_pointer += 1

        return max_profit