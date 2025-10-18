public class Solution {
    public int RemoveDuplicates(int[] nums) {
        if (nums.Length == 0)
        return 0;

    int uniqueIndex = 0;

    for (int i = 1; i < nums.Length; i++)
    {
        if (nums[i] != nums[uniqueIndex])
        {
            uniqueIndex++;
            nums[uniqueIndex] = nums[i];
        }
    }

    // After this, nums[0..uniqueIndex] contains unique elements
    return uniqueIndex + 1;
    }
}
