class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appeared = {}
        
        for n in nums:
            if n in appeared:
                return True
            else:
                appeared[n] = True
                
        return False