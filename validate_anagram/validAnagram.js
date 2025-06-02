/*
242. Valid Anagram
Solved
Easy
Topics
conpanies icon
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
*/

var isAnagram = function(s, t) {
    let s_array = Array.from(s).sort();
    let t_array = Array.from(t).sort();

    return JSON.stringify(s_array) === JSON.stringify(t_array)
}

console.log(isAnagram("anagram", "nagaram"))

console.log(isAnagram("rat", "car"))
