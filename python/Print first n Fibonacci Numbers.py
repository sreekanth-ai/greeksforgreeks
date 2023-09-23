class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        if n <= 0:
            return []

        # Initialize the list to store Fibonacci numbers
        fibonacci_list = [1, 1]
    
        # Generate Fibonacci numbers using dynamic programming
        for i in range(2, n):
            next_fibonacci = fibonacci_list[-1] + fibonacci_list[-2]
            fibonacci_list.append(next_fibonacci)
    
        return fibonacci_list[:n]
