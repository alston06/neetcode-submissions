class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        s = []
        i = j = 0
        while i < n or j < m:
            if i < n:
                s.append(word1[i])
            if j < m:
                s.append(word2[j])
            i+=1
            j+=1
        return "".join(s)