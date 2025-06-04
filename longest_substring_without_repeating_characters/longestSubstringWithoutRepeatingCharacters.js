/**
 * 3. Longest Substring Without Repeating Characters
Solved
Medium
Topics
conpanies icon
Companies
Hint
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
 */

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {

    if (!s) {
        return 0
    }

    let i = 0;
    let j = 1;
    let result = s[0];
    let temp = s[0];

    while (j < s.length) {
        if (!temp.includes(s[j])) {
            temp += s[j]
            j++;
        } else {
            i++;
            j = i + 1;
            temp = s[i];
        }

        if (temp.length > result.length) {
            result = temp;
        }
    }

    return result.length;
};

console.log(lengthOfLongestSubstring("abcabcbb")) // expect 3 for 'abc'

console.log(lengthOfLongestSubstring("bbbbb")) // expect 1 for 'b'

console.log(lengthOfLongestSubstring("pwwkew")) // expect 3 for 'wke'
