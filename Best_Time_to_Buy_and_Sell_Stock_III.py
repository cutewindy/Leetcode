# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most two transactions.

# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


# def maxProfit(prices):


def maxProfit(prices): 
    maxProfit = -1
    minPrice = prices[0]
    maxProfitForward = []
    for curPrice in prices:
        minPrice = min(minPrice, curPrice)
        maxProfit = max(maxProfit, curPrice - minPrice)
        maxProfitForward.append(maxProfit)

    maxProfit = -1
    maxPrice = prices[-1]
    maxProfitBackward = []
    for curPrice in reversed(prices):
        maxPrice = max(maxPrice, curPrice)
        maxProfit = max(maxProfit, maxPrice - curPrice)
        maxProfitBackward.append(maxProfit)

    maxProfit = maxProfitForward[-1]
    for i in range(len(prices) - 1):
        maxProfit = max(maxProfit, maxProfitForward[i] + maxProfitBackward[len(prices) - 2 - i])
    return maxProfit


print maxProfit([2, 0, 3, 4 ,6 ,1, 6])
print maxProfit([1, 2])












