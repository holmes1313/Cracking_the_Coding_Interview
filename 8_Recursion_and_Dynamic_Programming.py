# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:36:06 2019

@author: z.chen7
"""

# 8. Recursion and Dynamic Programming

# Interview Quesitons
import collections

# 8.1 Triple Step
def triple_step(n, memo={}):
    if n == 0:
        return 1
    
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    if n not in memo:
        memo[n] = triple_step(n-3) + triple_step(n-2) + triple_step(n-1)
    print(memo)
    return memo[n]

 
def triple_step2(n):
    if n < 2:
        return 1
    a = 1
    b = 1
    c = 2
    for i in range(3, n+1):
        c, b, a = a+b+c, c, b
    return c

triple_step(7) # 44
triple_step(7)


# Robot in a Grid
# Leetcode 63
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
"""
Example:
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""
def uniquePathsWithObstacles(obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rnum = len(obstacleGrid)
        cnum = len(obstacleGrid[0])
        # build dp matrix (rnum+1) * (cnum+1)
        dp = [[0 for c in range(cnum+1)] for r in range(rnum+1)]
        dp[0][1] = 1
        for i in range(1, rnum+1):
            for j in range(1, cnum+1):
                if obstacleGrid[i-1][j-1] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]


# 8.3 Magic Index
"""
Given that the array is sorted, it's very likely that we're supposed to use this condition.
As A is a sorted array of distinct integers, 
If A[index] > index,  the magic index must be on the left side.
If A[index] < index,  the magic index must be on the right side.
"""
def magicFast(array):
    left = 0
    right = len(array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if array[mid] == mid:
            return mid
        
        elif array[mid] < mid:
            left = mid + 1
            
        else:
            right = mid - 1
            
    return False

magicFast([-20,0,1,2,3,4,5,7,20])


# 8.4 Power Set
def powerSet(array):
    start = 0
    current = []
    result = []
    array.sort()
    backtrack(array, start, current, result)
    return result

# O(n 2^n)
def backtrack(array, start, current, result):
    result.append(current[:])
    for i in range(start, len(array)):
        if i > start and array[i] == array[i-1]:
            continue
        current.append(array[i])
        backtrack(array, i+1, current, result)
        current.pop()
        
powerSet([1,2,3])


# 8.5 Recursive Multiply
def minProduct(a, b):
    small = a if a < b else b
    large = a if a > b else b
    return minProduct_helper(small, large)
    
def minProduct_helper(small, large):
    if small == 0:
        return 0
    
    if small == 1:
        return large

    half = small // 2
    half_prod = minProduct_helper(half, large)
    
    if small % 2 == 1:
        return half_prod + half_prod + large
    else:
        return half_prod + half_prod
    

# 8.6 Towers of Hanoi
# pseudocode
"""
moveDisks(n, origin, destination, buffer):
    # base case
    if n <= 0:
        return 
        
    # move top n - 1 disks from origin to buffer, using destination as a buffer
    moveDisks(n-1, origin, buffer, destination)
    
    # move top from origin to destination
    moveTop(orgin, destination)
    
    # move top n-1 disks from buffer to destination, using origin as a buffer
    moveDisks(n-1, buffer, destination, origin)
"""

def moveDisks(n, origin, destination, buffer):
    if n <= 0:
        return
    
    #if n == 1:
        #destination.append(origin.pop())
        
    else:
        moveDisks(n-1, origin, buffer, destination)
        # moveDisks(1, origin, destination, buffer)
        destination.append(origin.pop())
        moveDisks(n-1, buffer, destination, origin)
        
    print('origin', origin)
    print('destination', destination)
    print('buffer', buffer)
    print('----')

moveDisks(3, [3,2,1], [], [])


# 8.7 Permutations without Dups
def permutationWithoutDups(array):
    current = []
    result = []
    backtrack_7(array, current, result)
    return result

def backtrack_7(array, current, result):
    if len(current) == len(array):
        result.append(current[:])
    else:
        for n in array:
            if n in current:
                continue
            current.append(n)
            backtrack_7(array, current, result)
            current.pop()

permutationWithoutDups([1,2,3])


# 8.8 Permutation with Dups
def permutationWithDups(array):
    current = []
    result = []
    counter = collections.Counter(array)
    backtrack_8(array, current, result, counter)
    return result

def backtrack_8(array, current, result, counter):
    if len(current) == len(array):
        result.append(current[:])
    else:
        for n in counter:
            if counter[n] > 0:
                current.append(n)
                counter[n] -= 1
                backtrack_8(array, current, result, counter)
                current.pop()
                counter[n] += 1

permutationWithDups([1,1,2])


# 8.9 Prens
class Solution_9(object):
    def generateParenthesis(self, n):
        if not n:
            return n
        left = right = n
        current = ''
        result = []
        self.dfs(left, right, current, result)
        return result

    def dfs(self, left, right, current, result):
        if right < left:
            return 

        if not left and not right:
            result.append(current)
        else:
            if left:
                self.dfs(left-1, right, current + '(', result)
            if right:
                self.dfs(left, right-1, current + ')', result)
                    

# 8.10 Paint Fill
def paintFill(image, sr, sc, newColor):
    if not image:
        return []

    oldColor = image[sr][sc]
    if oldColor != newColor:
        queue = collections.deque()
        queue.appendleft((sr, sc))
        while queue:
            m, n = queue.pop()
            image[m][n] = newColor
            for x, y in [(m-1, n), (m, n-1), (m, n+1), (m+1, n)]:
                if 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == oldColor:
                    queue.appendleft((x, y))

    return image


# 8.11 Coins
def coinChange(coins, amount, memo={}):
    
    if (amount, len(coins)) in memo:
        return memo[amount, len(coins)]
    
    if amount == 0:
        return 1
    
    if not coins:
        return 0
    
    coin = coins[-1]
    if coin == coins[0]:
        return 1 if amount % coin == 0 else 0
    
    numberOfWays = 0
    for cn in range(0, amount+1, coin):
        numberOfWays += coinChange(coins[:-1], amount-cn)
    memo[amount, len(coins)] = numberOfWays
    print(memo)    
    return numberOfWays


coinChange([1, 5, 10, 25], 25)




