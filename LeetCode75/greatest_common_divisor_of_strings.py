'''
1071. Greatest Common Divisor of Strings
Easy
Topics
Companies
Hint
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.

'''

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        if str1 + str2 != str2 + str1:
            return ''
        
        m = len(str1)
        n = len(str2)

        while m != n:
            if m > n:
                m -= n
            else:
                n -= m
        
        return str1[:m]


str1 = "ABCABC"
str2 = "ABC"
print(Solution().gcdOfStrings(str1, str2))

str1 = "ABABAB"
str2 = "ABAB"
print(Solution().gcdOfStrings(str1, str2))

str1 = "LEET"
str2 = "CODE"
print(Solution().gcdOfStrings(str1, str2))
