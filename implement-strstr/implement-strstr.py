class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return 0 if needle is '' else haystack.find(needle)