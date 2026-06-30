/**
 * @param {number[]} nums
 * @return {number}
 */
var minStartValue = function(nums) {
    const pre = [nums[0]];
    let minNum = pre[0];
    
    for(let i =1; i<nums.length; i++) {
        pre.push(pre[pre.length -1] + nums[i]);
        minNum = Math.min(minNum, pre[pre.length -1]);
    }
    
    return minNum <= 0 ? Math.abs(minNum) +1 : 1;
};
