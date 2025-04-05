'''
345. Reverse Vowels of a String
Easy
Topics
Companies
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left = 0
        right = len(s) - 1
        s_list = list(s)

        while left < right:
            left_c = s_list[left]
            right_c = s_list[right]
            if left_c in vowels and right_c in vowels:
                s_list[left] = right_c
                s_list[right] = left_c
                left += 1
                right -= 1
            elif left_c not in vowels:
                left += 1
            elif right_c not in vowels:
                right -= 1

        return ''.join(s_list)


print(Solution().reverseVowels("IceCreAm"))

print(Solution().reverseVowels("leetcode"))
