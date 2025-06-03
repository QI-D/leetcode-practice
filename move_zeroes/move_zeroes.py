'''
283. Move Zeroes
Easy
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

        pos = 0

        # set up a pointer to first remove all non-zero elements to the front
        # then fill rest of the list with 0
        for n in nums:
            if n != 0:
                nums[pos] = n
                pos += 1

        for i in range(pos, len(nums)):
            nums[i] = 0


if __name__ == "__main__":
    # nums = [0,1,0,3,12]
    nums = [0,0,1]
    print(Solution().moveZeroes(nums))