'''
643. Maximum Average Subarray I
Easy
Topics
conpanies icon
Companies
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
'''


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) == k:
            return float(sum(nums)) / k
        
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            # add new element nums[i], substract the element moved out of window nums[i-k]
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return float(max_sum) / k


nums = [1,12,-5,-6,50,3]
k = 4
print(Solution().findMaxAverage(nums, k))

nums = [5]
k = 1
print(Solution().findMaxAverage(nums, k))