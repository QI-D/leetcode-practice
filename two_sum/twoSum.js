/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {

    const numDict = {};

    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        const complement = target - num;

        if (complement in numDict) {
            return [numDict[complement], i];
        }

        numDict[num] = i;
    }
    
    return []
};

console.log(twoSum([2, 7, 11, 15], 9));
