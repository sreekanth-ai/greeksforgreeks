class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        incl_curr=a[0]
        excl_curr=0
        incl_prev=incl_curr
        excl_prev=excl_curr
        
        for i in range(1,n):
            excl_curr=max(incl_prev,excl_prev)

            incl_curr=excl_prev+a[i]
            
            excl_prev=excl_curr
            incl_prev=incl_curr
            
        return max(excl_curr,incl_curr)
