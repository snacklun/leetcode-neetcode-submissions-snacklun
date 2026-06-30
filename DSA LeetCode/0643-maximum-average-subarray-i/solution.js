/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    let left = 0;
    let curr = 0;
    let ans = 0;
    for (let i =0; i < k; i++) {
       curr += nums[i]; 
    }
    ans = curr / k;
    for (let right = k; right < nums.length; right++ ) {
        curr += nums[right] - nums[left];
        ans = Math.max(ans, curr/k);
        left++;
    }
    
    return ans;
};
