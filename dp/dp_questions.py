def fibMemoization(n, memo = {}):
    if n<=2:
        return 1
    
    if n in memo:
        return memo[n]
    memo[n] = fibMemoization(n-1, memo) + fibMemoization(n-2, memo)

    return memo[n]

def fibUsingTabulation(n):
    first = 1
    second = 1

    for index in range(2, n):
        current = first + second
        first = second
        second = current
    
    return second

def knapsack(profits, weights, capacity):
    # return knapsackBruteForce(profits, weights, capacity, 0)
    return knapsackMemoization(profits, weights, capacity, 0)

def knapsackBruteForce(profits, weights, capacity, currIndex):
    inbound = 0 <= currIndex < len(weights)
    if not inbound:
        return 0

    if capacity <=0:
        return 0

    profit1 = 0
    currentWeight = weights[currIndex]
    if currentWeight <= capacity:
        profit1 = profits[currIndex] + knapsackBruteForce(profits, weights, 
        capacity-currentWeight, currIndex + 1)
    profit2 = knapsackBruteForce(profits, weights, capacity, currIndex+1)

    return max(profit1, profit2)


def knapsackMemoization(profits, weights, capacity, currIndex, memo={}):
    inbount = 0 <= currIndex < len(weights)
    if not inbount:
        return 0
    
    if capacity <=0:
        return 0
    
    key = (capacity, currIndex)

    if key in memo:
        return memo[key]
    withCurrentWeightProfit = 0
    if weights[currIndex] <= capacity:
        withCurrentWeightProfit = profits[currIndex] + knapsackMemoization(profits,
        weights, capacity -weights[currIndex], currIndex+1)
    withoutCurrentWeightProfit = knapsackMemoization(profits, weights, capacity, currIndex+1)

    return max(withCurrentWeightProfit, withoutCurrentWeightProfit)

def knapsackTabulations(profits, weights, capacity):
    """TODO- implement using tabulations method"""
    pass

def canSumMemoization(target, nums, memo={}):
    if target == 0:
        return True
    
    if target < 0:
        return False
    
    if target in memo:
        return memo[target]
    
    for num in nums:
        if canSumMemoization(target-num, nums, memo):
            memo[target] = True
            return memo[target]
    
    memo[target] = False
    return memo[target]


def canSumTabulation(target, nums):
    dp = [False for n in range(target+1)]
    dp[0] = True

    for index in range(target):
        if dp[index]:
            for num in nums:
                if index+num < len(dp):
                    dp[index+num] = True
    
    return dp[target]

def howSumMemoization(target, nums, memo={}):
    if target==0:
        return []
    
    if target < 0:
        return # it is not possible to have some on this path
    
    if target in memo:
        return memo[target]
    for num in nums:
        result = howSumMemoization(target-num, nums)
        if result:
            result.append(num)
            return result

    memo[target] = None
    return memo[target]



            
    
    