class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle is '':
            return 0
        return haystack.find(needle)