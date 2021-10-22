class Solution:
    def frequencySort(self, s: str) -> str:
        hist = {} # histogram
        
        for char in s:     
            try:
                hist[char] += 1
            except:
                hist[char] = 1
                
        sort_hist = reversed(sorted(hist, key=hist.get))
        
        res = ''
        
        for key in sort_hist:
            for i in range(hist[key]):
                res = f'{res}{key}'
                
        return res