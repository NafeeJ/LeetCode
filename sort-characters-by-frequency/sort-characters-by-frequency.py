class Solution:
    def frequencySort(self, s: str) -> str:
        hist = {} # histogram
        
        for char in s:     
            try:
                hist[char] += 1
            except:
                hist[char] = 1
                
        sort_hist = sorted(hist, key=hist.get)
        
        res = ''
        
        for key in sort_hist[::-1]:
            for i in range(hist[key]):
                res = f'{res}{key}'
                
        return res