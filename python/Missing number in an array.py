class Solution:
    def missingNumber(self,array,n):
        # code here
        tot = 0
        for i in range(n-1):
            tot += array[i]
        return int(((n*(n+1))/2) - tot)
