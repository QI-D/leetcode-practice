'''
7. Reverse Integer
Medium
Topics
Companies
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign = -1 if x < 0 else 1
        result = int(str(abs(x))[::-1]) * sign

        if result >= 2**31-1 or result <= -2**31:
            return 0

        return result



x = 123
print(Solution().reverse(x))

x = -123
print(Solution().reverse(x))

x = 120
print(Solution().reverse(x))

x = 1534236469
print(Solution().reverse(x))