'''
5. Longest Palindromic Substring
Medium
Topics
Companies
Hint
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s

        def expand_from_center(left, right):
            # expand as long as it's a valid palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # return longest palindrome found
            return s[left + 1:right]

        result = ""

        for i in range(len(s)):
            # odd length palindrome centered at s[i]
            odd_palindrom = expand_from_center(i, i)
            if len(odd_palindrom) > len(result):
                result = odd_palindrom

            # even length palindrome centered between s[i] and s[i+1]
            even_palindrome = expand_from_center(i, i +1 )
            if len(even_palindrome) > len(result):
                result = even_palindrome

        return result


print(Solution().longestPalindrome("babad"))

print(Solution().longestPalindrome("cbbd"))

print(Solution().longestPalindrome("a"))
