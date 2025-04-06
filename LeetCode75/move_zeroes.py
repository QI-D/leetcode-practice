'''
283. Move Zeroes
Solved
Easy
Topics
Companies
Hint
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        nonzero = 0
        i = 0

        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[nonzero] = nums[nonzero], nums[i]

                nonzero += 1

            i += 1
        print(nums)


Solution().moveZeroes([0,1,0,3,12]) # expect [1,3,12,0,0]

Solution().moveZeroes([0]) # expect [0]
