'''
1456. Maximum Number of Vowels in a Substring of Given Length
Medium
Topics
conpanies icon
Companies
Hint
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
'''

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        if k > len(s):
            return -1

        vowels = set('aeiou')
        count = 0
        max_count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = count

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            max_count = max(max_count, count)

        return max_count

s = "abciiidef"
k = 3
print(Solution().maxVowels(s, k)) # expect 3 as the substring "iii" contains 3 vowel letters

s = "aeiou"
k = 2
print(Solution().maxVowels(s, k)) # expect 3 as any substring of length 2 contains 2 vowels

s = "leetcode"
k = 3
print(Solution().maxVowels(s, k)) # expect 3 as "lee", "eet" and "ode" contain 2 vowels
