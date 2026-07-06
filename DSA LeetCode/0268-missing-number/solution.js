/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    const n = nums.length;
    const defaultSet = new Set(Array.from({ length: n + 1 }, (_, i) => i));
    console.log(defaultSet)
    for( num of nums) {
        if (defaultSet.has(num)) {
            defaultSet.delete(num);
        }
    }
    
    return [...defaultSet][0]
};
