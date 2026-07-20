class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(len(s)-1):
            j = ord(s[i])
            k = ord(s[i+1])
            sum += abs(k-j)
        return sum
