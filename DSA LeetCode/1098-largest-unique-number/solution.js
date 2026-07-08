/**
 * @param {number[]} nums
 * @return {number}
 */
var largestUniqueNumber = function(nums) {
    const newMap = new Map();

    for(const num of nums) {
        newMap.set(num, ( newMap.get(num) ||0) + 1);    
    }
    
    let res = -1;
    for (const [k,v] of newMap) {
        if (v === 1 && k > res) {
            res = k;
        }
    }
    return res;
};
