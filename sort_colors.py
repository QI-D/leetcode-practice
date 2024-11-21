'''
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        for i in range(1, len(nums)):
            a = nums[i]  

            # Move elements of list1[0 to i-1],
            # which are greater to one position
            # ahead of their current position
            j = i - 1

            while j >= 0 and a < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1

            nums[j + 1] = a

        return nums


if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    result = Solution().sortColors(nums)

    print(result)
