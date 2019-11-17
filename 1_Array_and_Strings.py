# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 10:11:58 2019

@author: z.chen7
"""
# 1. Array and Strings

# Hash Tables
"""
A hash table is a data structure that maps keys to valus for highly efficient lookup.

Implementation (an array of linked lists and a hash code function)
1. compute the key's hash code
2. map the hash code to an index in the array, hash(key) % bucket_num
3. store the key and value in a linked list in this index
"""


# Interview Questions
import collections
import unittest


# 1.1 Is Unique
def unique(word):
    hashtable = {}
    for char in word:
        if char in hashtable :
            return False
        hashtable[char] = 1
    return True


# 1.2 Check Permutation
def check_permutation(word1, word2):
    if len(word1) != len(word2):
        return False
    counter1 = collections.Counter(word1)
    counter2 = collections.Counter(word2)
    return counter1 == counter2


# 1.3 URLify
def urlify(string, length):
    """
    :type string: list
    :type length: int
    :rtype:list
    """
    new_index = len(string)
    
    for i in range(length-1, -1, -1):
        if string[i] != " ":
            # Move characters
            string[new_index-1] = string[i]
            new_index -= 1
        else:
            # Replace spaces
            string[new_index-3: new_index] = '%20'
            new_index -= 3
            
    return string
    
# note         
a = ['a', 'b', 'c', 'e']            
a[:3] = 'mx'  # ['m', 'x', 'e']

if " ":
    print("Space is not an empty string!")
    
if "":
    print("nothing!")
    
    
# 1.4 Palindrom Permutation
def pal_perm(string):
    '''function checks if a string is a permutation of a palindrome or not'''
    counter = collections.Counter(string.replace(" ", "").lower())
    
    if len(string.replace(" ", "").lower()) % 2:
        odd_count = 1
    else:
        odd_count = 0
    
    for char in counter:
        if counter[char] % 2 == 1:
            odd_count -= 1
            if odd_count < 0:
                return False
    return True


# 1.5 One Away
def one_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    
    short, long = sorted([s1, s2], key=len)
    counter = collections.Counter(long)
    
    for char in short:
        if char in counter:
            counter[char] -= 1
            if counter[char] == 0:
                del counter[char]
                
    return len(counter) < 2
    
    
# 1.6 String Comprehension
def string_compression(string):
    lo = hi = 0
    result = ""
    
    while hi < len(string):
        char = string[hi]
        count = 0
        while hi < len(string) and string[hi] == char:
            count += 1
            hi += 1
        result += string[lo] + str(count)
        lo = hi
        
    return result if len(result) < len(string) else string
    

def string_compression2(string):
    compressed = []
    counter = 0
    
    for i in range(len(string)):
        if i != 0 and string[i] != string[i-1]:
            compressed.append(string[i-1] + str(counter))
            counter = 0
        counter += 1
    # add last repeated character
    compressed.append(string[-1] + str(counter))
    print(compressed)
    return ''.join(compressed)
    
    
# 1.7 Rotate Matrix
def rotate_matrix(matrix):
    return [list(row[::-1]) for row in list(zip(*matrix))]


def rotate_matrix2(matrix):
    # in place
    # revserse the matrix
    matrix = matrix[::-1]
    for i in range(len(matrix)-1):
        for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix
    

# 1.8 Zero Matrix
def zero_matrix(matrix):
    rows = []
    cols = []
    # Try finding the cells with zeros first before making any changes to the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.append(i)
                cols.append(j)
                
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in rows or j in cols:
                matrix[i][j] = 0
    print(rows)
    print(cols)
    return matrix


# 1.9 String Rotation
def is_substring(string, sub):
    return string.find(sub) != -1
    
    
def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return is_substring(s1+s1, s2)
    

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]
    
    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)
    
if __name__ == "__main__":
    unittest.main()
    
    
    
    