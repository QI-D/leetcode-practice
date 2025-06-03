'''
383. Ransom Noet

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        sorted_ransomNote = sorted(ransomNote)
        sorted_magazine = sorted(magazine)

        index = 0
        for c in sorted_magazine:
            if index < len(sorted_ransomNote) and sorted_ransomNote[index] == c:
                index += 1

        return index == len(sorted_ransomNote)


if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "ab"

    result = Solution().canConstruct(ransomNote, magazine)
    print(result)