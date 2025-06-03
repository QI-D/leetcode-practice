'''
409. Longest Palindrome
Easy
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_count = {}
        for c in s:
            if c not in char_count:
                char_count[c] = 1
            else:
                char_count[c] += 1

        max_length = 0
        odd_found = False

        for count in char_count.values():
            if count % 2 == 0:
                max_length += count
            else:
                max_length += count-1
                odd_found = True

        if odd_found:
            max_length += 1

        return max_length


if __name__ == "__main__":
    # s = "abccccdd"
    s = "aA"
    print(Solution().longestPalindrome(s))