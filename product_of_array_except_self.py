'''
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the 
elements of nums except nums[i].

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
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as 
extra space for space complexity analysis.)
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n  # Initialize answer array with 1s

        # First pass: calculate products of elements to the left of each index
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        # Second pass: multiply by the products of elements to the right of each index
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer


if __name__ == "__main__":
    nums = [0, 1]
    result = Solution().productExceptSelf(nums)
    print(result)