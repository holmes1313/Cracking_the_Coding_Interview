# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 18:09:44 2019

@author: z.chen7
"""

# 10. Sorting and Searching
"""
Merge sort
Merge sort divides the array in halves, sort each of those halves, and then 
merge them back together. Each of those halves has the same sorting algorithm
applied to it.
"""

def mergesort(array):
    if len(array) > 1:
        mid = len(array) // 2   # **
        L = array[:mid]
        R = array[mid:]
       
        mergesort(L)
        mergesort(R)
        
        i = j = k = 0
        
        while (i < len(L)) and (j < len(R)):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
            
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
            
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
                
a = [3, 2,1]
mergesort(a)
a


# quicksort
"""
In quick sort, we pick a random element, pivot, and divide the arrary to three groups
greater than, less than and equal to. And we apply the same algorithm to the greater
and less groups, the array will eventually become sorted.

Runtime: O(n logn) average, O(n^2) worst case, memory O(log(n))
"""
def quicksort(array):
    # base case
    if len(array) < 2:
        return array
    
    less = []
    greater = []
    equal = []
    
    pivot = array[1]
    
    for x in array:
        if x < pivot:
            less.append(x)
        elif x > pivot:
            greater.append(x)
        else:
            equal.append(x)
            
    return quicksort(less) + equal + quicksort(greater)

quicksort([4, 3, 2, 1])



# Binary search
"""
In binary search, we look for an element x in a sorted array by first comparing
x to the midpoint of the array. If x is less than the midpoint, we search the left
half of the array. If x is greater the midpoint, we search the right half of
the array. Then we repeat the process, treating the left and right halves as the
subarrays."""

def binarySearch(array, x):
    low = 0
    high = len(array) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if x < array[mid]:
            high = mid - 1
        elif x > array[mid]:
            low = mid + 1
        else:
            return mid    
    return -1


def binarySearchRecursive(array, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if array[mid] < target:
        return binarySearchRecursive(array, target, mid + 1, high)
    elif array[mid] > target:
        return binarySearchRecursive(array, target, low, mid - 1)
    else:
        return mid

binarySearch([1,2, 3,4, 5], 5)
binarySearchRecursive([1,2, 3,4, 5], 5,0,4)


# Interview Questions

# 10.1 Sorted Merge
class Solution1(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        indexMerged = m + n - 1
        index1 = m - 1
        index2 = n - 1
        
        while index1 >= 0 and index2 >= 0:
            if nums1[index1] > nums2[index2]:
                nums1[indexMerged] = nums1[index1]
                index1 -= 1
            else:
                nums1[indexMerged] = nums2[index2]
                index2 -= 1
            indexMerged -= 1
        
        while index2 >= 0:
            nums1[indexMerged] = nums2[index2]
            index2 -= 1
            indexMerged -= 1
    
    
# 10.2 Group Anagrams
strings = ["cat", "bat", "rat", "arts", "tab", "tar", "car", "star"]
sorted(strings, key=sorted)
# ['bat', 'tab', 'car', 'cat', 'arts', 'star', 'rat', 'tar']



# 10.3 Search in Rotated Array
class Solution3(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:  # Found
                return mid
            if nums[low] < nums[mid]:  # Left is normally ordered
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] < nums[high]:  # Right is normally ordered
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] == nums[mid]:  # search right
                    low = mid + 1
                if nums[mid] == nums[high]:  # search left
                    high = mid - 1
        return -1


# 10.4 Sorted Search, No Size
# Leetcode 702
"""
The problem is that binary search requires us knowing the length of the list,
so that we can compare it to the target to the midpoint.
It's better to back off exponentially. Try 1, then 2, then 4, then 8 and so on.
This ensures that if the list has length n, we'll find the length in at most
O(log n) time.
Once we find the length, we just perform a (mostly) normal binary search
"""

class Solution_4(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        index = 1
        # in the processs, if the element is bigger than target
        # we'll jump over to the binary search part early
        while reader.get(index) < 10000 and reader.get(index) < target:
            index *= 2
        
        # we only need to check between index // 2 and index
        # because the previous iteration ensured reader.get(index // 2) < target
        low = index // 2
        high = index
        while low <= high:
            mid = (low + high) // 2
            middle = reader.get(mid)
            if middle == target:
                return mid
            elif target < middle:
                high = mid - 1
            else:
                low = mid + 1
        return -1
            

# 10.5 Sparse Search
"""
Need to fix the comparison against mid, in case mid is an empty string.
We simply move mid to the closest non-empty string.
"""
def sparseSearch(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if not array[mid]:   #  move mid to the closest non-empty string
            left = mid - 1
            right = mid + 1
            while left >= low or right <= high:
                if left >= low and array[left]:
                    mid = left
                    break
                elif right <= high and array[right]:
                    mid = right
                    break
                left -= 1
                right += 1
        if array[mid] == target:
            return mid
        if array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
    
    
sparseSearch(['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '', 'mom'], 'at')    
sparseSearch(['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '', 'mom'], 'ball')    
sparseSearch(['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '', 'mom'], 'car')    
sparseSearch(['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '', 'mom'], 'dad')        
sparseSearch(['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '', 'mom'], 'mom')  
sparseSearch(['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '', 'mom'], 'me')    
sparseSearch(["", "", "", ""], 'mom')    
   
    

# leetcode 74
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        nrow = len(matrix)
        ncol = len(matrix[0])
        
        low = 0
        high = nrow * ncol - 1
        
        while low <= high:
            print('low', low)
            print('high', high)
            mid = (low + high) // 2
            print('mid',mid)
            middle = matrix[mid // ncol][mid % ncol]
            
            if middle == target:
                return True
            
            if target < middle:
                high = mid - 1
            
            else:
                low = mid + 1
                
        return False


