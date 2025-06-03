/**
 * 76. Minimum Window Substring
Hard
Topics
conpanies icon
Companies
Hint
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
 */

/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    // Create frequency map of characters we need to find
  const targetChars = {};
  for (const char of t) {
    targetChars[char] = (targetChars[char] || 0) + 1;
  }
  
  // Number of unique characters we need to match
  let required = Object.keys(targetChars).length;
  // Sliding window pointers
  let left = 0, right = 0;
  // Count of how many required characters we've matched
  let formed = 0;
  // Store window character counts
  const windowCounts = {};
  // Result storage [length, left index, right index]
  let result = [-1, 0, 0];
  
  // Expand the window by moving right pointer
  while (right < s.length) {
    const char = s[right];
    // Increment count for this character in window
    windowCounts[char] = (windowCounts[char] || 0) + 1;
    
    // If we've reached the required count for this character
    if (targetChars[char] && windowCounts[char] === targetChars[char]) {
      formed++;
    }
    
    // Try to contract the window from the left
    while (left <= right && formed === required) {
      const currentLength = right - left + 1;
      
      // Update result if we found a smaller valid window
      if (result[0] === -1 || currentLength < result[0]) {
        result = [currentLength, left, right];
      }
      
      // The character at the left pointer
      const leftChar = s[left];
      // Decrease its count in window since we're moving left
      windowCounts[leftChar]--;
      
      // If we no longer have enough of this character
      if (targetChars[leftChar] && windowCounts[leftChar] < targetChars[leftChar]) {
        formed--;
      }
      left++;
    }
    right++;
  }
  
  // Return the found substring or empty string if none found
  return result[0] === -1 ? "" : s.slice(result[1], result[2] + 1);
};

console.log(minWindow("ADOBECODEBANC", "ABC"))
