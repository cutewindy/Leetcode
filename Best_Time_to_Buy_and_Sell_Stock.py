# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell 
# one share of the stock), design an algorithm to find the maximum profit.

def maxProfit(prices):
    price = 0
    if len(prices) < 2:
        return 0
    else:
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > price:
                    price = prices[j] - prices[i]
        return price



print maxProfit([])
print maxProfit([4, 3, 1, 5, 2, 6])
print maxProfit([6, 2, 3, 5, 1, 4, 5, 3])


def maxProfitI(prices):
    maxi = 0
    if len(prices) < 2:
        return maxi
    else:
        mini = prices[0]
        maxi = 0
        for i in range(1, len(prices)):
            mini = min(mini, prices[i-1])
            maxi = max(maxi, prices[i] - mini)
        return maxi


print maxProfitI([])
print maxProfitI([4, 3, 1, 5, 2, 6])
print maxProfitI([6, 2, 3, 5, 1, 4, 5, 3])







