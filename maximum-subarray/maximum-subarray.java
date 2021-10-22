class Solution {
    public int maxSubArray(int[] nums) {
        int max_sum = nums[0];
        int cur_sum = 0;
        
        for (int i : nums) {
            if (cur_sum < 0)
                cur_sum = 0;
            cur_sum += i;
            max_sum = Math.max(max_sum, cur_sum);
        }
        
        return max_sum;
    }
}