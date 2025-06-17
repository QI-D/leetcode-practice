'''
394. Decode String
Medium
Topics
conpanies icon
Companies
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
'''

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count_stack = []
        string_stack = []
        current_string = ''
        current_num = 0

        for c in s:
            if c.isdigit():
                current_num = current_num * 10 + int(c) # handle multi-digit numbers
            elif c == '[':
                count_stack.append(current_num)
                string_stack.append(current_string)
                current_num = 0
                current_string = ''
            elif c == ']':
                repeat_times = count_stack.pop()
                previous_string = string_stack.pop()
                current_string = previous_string + current_string * repeat_times
            else:
                current_string += c

        return current_string


s = "3[a]2[bc]"
print(Solution().decodeString(s)) # expect "aaabcbc"

s = "3[a2[c]]"
print(Solution().decodeString(s)) # expect "accaccacc"

s = "2[abc]3[cd]ef"
print(Solution().decodeString(s)) # expect "abcabccdcdcdef"
