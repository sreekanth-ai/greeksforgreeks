class Solution:
    def kthSmallest(self,arr, l, r, k):
        arr.sort()
        return arr[k-1]
