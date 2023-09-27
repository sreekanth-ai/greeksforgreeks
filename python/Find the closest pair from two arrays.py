class Solution:
    def printClosest (self,arr, brr, n, m, x) : 
        # code here
        n, m = m, n
        diff = float("inf")
        res_l, res_r = 0, 0
        l, r = 0, n - 1

        while l < m and r >= 0:
            if abs(arr[l] + brr[r] - x) < diff:
                res_l, res_r = l, r
                diff = abs(arr[l] + brr[r] - x)
            if arr[l] + brr[r] > x:
                r -= 1
            else:
                l += 1
        result = [arr[res_l], brr[res_r]]
        return result

