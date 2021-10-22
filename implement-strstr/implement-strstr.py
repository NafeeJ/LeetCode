class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle is '':
            return 0
        needle_len = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i + needle_len] == needle:
                return i
        return -1