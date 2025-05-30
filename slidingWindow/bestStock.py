def maxProfit(prices: list[int]) -> int:
    l, r = 0, 1

    currentMax = 0
    while (r < len(prices)):

        if (prices[l] < prices[r]):
            if (prices[r] - prices[l] > currentMax):
                currentMax = prices[r] - prices[l]

            r += 1
        elif (prices[l] > prices[r]):

            l = r
            r += 1
        else:
            r += 1

    return currentMax


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))
print(maxProfit([2, 1, 2, 1, 0, 1, 2]))
