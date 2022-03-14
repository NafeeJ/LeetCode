/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    cache = new Map()
    for (let i = 0; i < nums.length; i++) {
        b = target - nums[i]
        if (cache.has(b)) {
            return [cache.get(b), i]
        }
        else {
            cache.set(nums[i], i)
        }
    }
};