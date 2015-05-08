# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
# (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple 
# transactions at the same time (ie, you must sell the stock before you buy again).


def maxProfit(prices):
    earn = 0
#     if len(prices) == 0 or len(prices) == 1:
#         return earn
#     elif len(prices) == 2 and prices[0] <= prices[1]:
#         return prices[1] - prices[0]
#     elif len(prices) > 2:
#         if prices[0] <= prices[1]:
#             earn -= prices[0]
#         for i in range(1, len(prices) - 1):
#             if prices[i - 1] > prices[i] and prices[i] <= prices[i + 1]:
#                 earn -= prices[i] 
#             if prices[i - 1] < prices[i] and prices[i] >= prices[i + 1]:
#                 earn += prices[i]  
#         if prices[len(prices) - 2] < prices[len(prices) - 1]:
#             earn += prices[len(prices) - 1]

    for i in range(len(prices)-1):
        if prices[i] < prices[i + 1]:
            earn += prices[i+1] - prices[i]
    return earn

     
print maxProfit([2, 1, 3, 4, 5, 2, 1])
print maxProfit([2, 1, 3, 4, 5, 1, 2])
print maxProfit([])
print maxProfit([2, 2, 5])
print maxProfit([3, 3])
print maxProfit([2, 2])

