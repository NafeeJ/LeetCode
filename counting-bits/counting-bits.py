class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        
        for i in range(0, n+1):
            ones = 0
            for bit in bin(i)[2:]:
                if (bit == "1"):
                    ones += 1
            ans.append(ones)
        return ans