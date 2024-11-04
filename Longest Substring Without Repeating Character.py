#Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s=list(s)
        strin=[]
        maxlen=0
        l=0
        for r in range(len(s)):
            if s[r] not in strin:
                strin.append(s[r])
            else:
                while s[r] in strin:
                    strin=strin[1:]
                    l+=1
                strin.append(s[r])
            maxlen=max(maxlen,len(strin))
        return maxlen