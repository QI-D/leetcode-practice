/**
 * 49. Group Anagrams
Solved
Medium
Topics
conpanies icon
Companies
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
 */

/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {

    let result_map = {};
    let result_array = [];

    for (let str of strs) {
        sorted_str = str.split('').sort().join('');
        if (!(sorted_str in result_map)) {
            result_map[sorted_str] = [str];
        } else {
            result_map[sorted_str].push(str);
        }
        
    }

    for (let k in result_map) {
        result_array.push(result_map[k]);
    }

    return result_array;
};

// expect [["bat"],["nat","tan"],["ate","eat","tea"]]
console.log(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
