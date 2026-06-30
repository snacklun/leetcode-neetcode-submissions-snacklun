/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let ans = [nums[0]];
    for(let i = 1; i < nums.length; i++) {
        ans.push(ans[i-1] + nums[i] );
    }
    
    return ans;
};
