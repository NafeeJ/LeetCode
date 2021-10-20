class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        # Given that n = target - m, where n and m are any two numbers:
        for i, n in enumerate(nums):
            m = target - n
            if m in cache:
                return [cache[m], i]
            else:
                cache[n] = i
        return null