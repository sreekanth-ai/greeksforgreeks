class Solution:
    def colName (self, n):
        # your code here
        res = ""
        while n>0:
            n -= 1
            temp = n%26
            res += chr(ord('A') + temp)
            n //= 26
        return res[::-1]
