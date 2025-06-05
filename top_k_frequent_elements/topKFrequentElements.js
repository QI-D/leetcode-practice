/**
 * 347. Top K Frequent Elements
Medium
Topics
conpanies icon
Companies
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
 */

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let countMap = {};
    let result = [];

    if (nums.length == k) {
        return nums;
    }

    for (let num of nums) {
        if (!(num in countMap)) {
            countMap[num] = 1;
        } else {
            countMap[num] += 1;
        }
    }

    // sort the countMap by value in descending order
    // sortedCountMap is an array of [key, value] pairs. (i.e. [ ['1', 3], ['2', 2], ['3', 1] ])
    const sortedCountMap = Object.entries(countMap)
        .sort(([, valueA], [, valueB]) => valueB - valueA);

    for (let i = 0; i < k; i++) {
        result.push(Number(sortedCountMap[i][0]));
    }

    return result;
};

console.log(topKFrequent([1,1,1,2,2,3], 2)) // expect [1, 2]

console.log(topKFrequent([1], 1)) // expect [1]

console.log(topKFrequent([3,0,1,0], 1)) // expect [0]
