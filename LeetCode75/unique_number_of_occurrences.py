'''
1207. Unique Number of Occurrences
Easy
Topics
conpanies icon
Companies
Hint
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
'''

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = {}

        for num in arr:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        values = list(count.values())

        return len(values) == len(set(values))


arr = [1,2,2,1,1,3]
print(Solution().uniqueOccurrences(arr)) # expect true

arr = [1,2]
print(Solution().uniqueOccurrences(arr)) # expect false

arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(Solution().uniqueOccurrences(arr)) # expect true
