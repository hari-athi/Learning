# Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        lists = s.split()
        return " ".join(lists[::-1])

