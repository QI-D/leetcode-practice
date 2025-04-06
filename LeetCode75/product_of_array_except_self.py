'''
238. Product of Array Except Self
Solved
Medium
Topics
Companies
Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # approach 1:
        # n = len(nums)
        # result = [1] * n

        # for i in range(n):
        #     product = 1
        #     for j in range(n):
        #         if i != j:
        #             product *= nums[j]
        #     result[i] = product

        # return result

        # approach 2:
        n = len(nums)
        result = [1] * n

        left_product = 1
        for i in range(n):
            result[i] = left_product # store current product of elements to the left
            left_product *= nums[i] # update left_product to include nums[i] for the next iteration

        right_product = 1
        for i in reversed(range(n)):
            result[i] *= right_product # multiply current value by right product
            right_product *= nums[i] # update right product for next iteration

        return result

print(Solution().productExceptSelf([1,2,3,4]))

print(Solution().productExceptSelf([-1,1,0,-3,3]))
