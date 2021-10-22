class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_len = len(nums)
        left = [1] * num_len
        right = [1] * num_len
        
        left.append(1)
        for i in range(1, num_len):
            left[i] = left[i - 1] * nums[i - 1]
        
        right[num_len - 1] = 1
        for i in range(num_len)[-2::-1]:
            right[i] = right[i + 1] * nums[i + 1]
        
        res = [1] * num_len
        for i in range(num_len):
            res[i] = left[i] * right[i]
            
        return res