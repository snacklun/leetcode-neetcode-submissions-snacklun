/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxLength = function(nums) {
    const newMap = new Map();
    let cnt = 0;
    let res = 0;
    
    for (let i = 0; i< nums.length; i++) {
        cnt += (nums[i] === 1) ? 1 : -1;
        if (cnt === 0) {
           res = Math.max(res, i+1);
        }
        if (newMap.has(cnt)) {
            res=Math.max(res, i- newMap.get(cnt))
        } else {
          newMap.set(cnt, i)
        }
    }

    return res;
};
