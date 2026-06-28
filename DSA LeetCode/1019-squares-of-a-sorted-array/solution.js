/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let i = 0;
    let j = nums.length - 1;
    let res = new Array();
    // square
    while (i < j) {
        const a =  nums[i] * nums[i];
        const b =  nums[j] * nums[j];
        res[i] = a;
        res[j] = b;
     
        i++;
        j--;
        
    }
    if (i === j) {
        res[i] =  nums[i] * nums[i];
    }
    res.sort((a,b) => a-b);
    
    return res;
};
