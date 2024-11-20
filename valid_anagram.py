'''
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and 
false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? 
How would you adapt your solution to such a case?
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        s_list = [i for i in s]
        t_list = [i for i in t]

        if sorted(s_list) == sorted(t_list):
            return True
        return False

if __name__ == "__main__":
    # s = "anagram"
    # t = "nagaram"

    s = "rat"
    t = "car"

    result = Solution().isAnagram(s, t)
    print(result)