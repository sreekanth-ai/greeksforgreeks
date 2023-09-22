class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        total_sum = sum(A)
        left_sum = 0
        
        for i in range(N):
            total_sum -= A[i]
            
            if left_sum == total_sum:
                # Equilibrium point found, return 1-based index
                return i + 1
            
            left_sum += A[i]
        
        # No equilibrium point found
        return -1
