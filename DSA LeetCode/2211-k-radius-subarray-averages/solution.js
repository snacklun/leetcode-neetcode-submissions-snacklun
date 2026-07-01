/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var getAverages = function(nums, k) {
    let left = 0;
    let right = 2*k;
    let ans = [];
    let isFirst = true;
    let curr =0;
    if (k === 0 && nums.length === 1) {
        return [nums[0]];
    }
    for(let i = 0; i < nums.length; i++) {
        if (i < k || i + k > nums.length -1) {
            ans[i] = -1;
            continue;
        }
        
        if (isFirst) {
  
            for(let j = 0; j<2*k + 1;j++){
                curr+=nums[j];
            }
            ans[i] =Math.floor(curr/(2*k+1));
            isFirst = false;
        } else {
            curr = curr + nums[right] - nums[left -1 ];
            ans[i] =Math.floor(curr/(2*k+1));
        }
        right++;
        left++;
    }
    return ans;
    
};
