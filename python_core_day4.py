#Function that finds maximum difference between two elements where larger comes after smaller
def Diff(nums):
    minDiff = 0
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                minDiff = max(minDiff, nums[j] - nums[i])
    return minDiff


#Function that returns all pairs (i, j) such that arr[j] > arr[i] and j > i
def Greater(nums):
    pairs = []
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i] and j > i:
                pairs.append((i, j))
    return pairs


#Leetcode-121 Best Time to Buy and sell stocks
def TimeToBuySell(nums):
    maxProfit = 0
    bestBuy = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > bestBuy:
            maxProfit = max(maxProfit, nums[i]-bestBuy)
        bestBuy = min(nums[i], bestBuy)
    return maxProfit

hehe = TimeToBuySell([7, 1, 3, 6, 8])
print(hehe)