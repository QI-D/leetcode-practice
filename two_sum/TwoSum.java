// 1. Two Sum
// Solved
// Easy
// Topics
// Companies
// Hint
// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// You can return the answer in any order.

// Example 1:

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
// Example 2:

// Input: nums = [3,2,4], target = 6
// Output: [1,2]
// Example 3:

// Input: nums = [3,3], target = 6
// Output: [0,1]

// Constraints:

// 2 <= nums.length <= 104
// -109 <= nums[i] <= 109
// -109 <= target <= 109
// Only one valid answer exists.

// Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

package two_sum;

import java.util.Arrays;

import java.util.HashMap;
import java.util.Map;

class TwoSum {
    // public int[] twoSum(int[] nums, int target) {
    // int n = nums.length;
    // int[] result = new int[2];
    // for (int i = 0; i < n - 1; i++) {
    // for (int j = i + 1; j < n; j++) {
    // if (nums[i] + nums[j] == target) {
    // result[0] = i;
    // result[1] = j;
    // return result;
    // }
    // }
    // }
    // return new int[] {};
    // }

    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numDict = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            if (numDict.containsKey(complement)) {
                return new int[] { numDict.get(complement), i };
            }

            numDict.put(nums[i], i);
        }

        return new int[] {};
    }

    public static void main(String[] args) {

        int arr[] = { 2, 7, 11, 15 };
        int target = 9;

        TwoSum ts = new TwoSum();
        int result[] = ts.twoSum(arr, target);

        System.out.println(Arrays.toString(result));
    }
}
