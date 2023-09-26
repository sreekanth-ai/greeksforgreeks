import heapq
class findMaxSum:
    def __init__(self, A, B):
        # Sort the lists in reverse order
        self.A = sorted(A, reverse=True) 
        self.B = sorted(B, reverse=True)
        self.sums, self.visited = list(), set()
        self.__add_element(0, 0)
        
    def __call__(self):
        # Pop the element with the maximum sum
        el_sum, indexes = heapq.heappop(self.sums)
        iA, iB = indexes
        # Add the next possible elements to the heap
        self.__add_element(iA, iB + 1)
        self.__add_element(iA + 1, iB)
        return -el_sum
        
    def __add_element(self, iA, iB):
        indexes = iA, iB
        # Check if the indexes are within range and not already visited
        if iA < len(self.A) and iB < len(self.B) and indexes not in self.visited:
            # Push the sum and indexes to the heap
            heapq.heappush(self.sums, (-self.A[iA] - self.B[iB], indexes))
            self.visited.add(indexes)

class Solution:
    # Function to find the maximum combinations with maximum sum
    def maxCombinations(self, N, K, A, B):
        # Create an instance of findMaxSum class
        retriver = findMaxSum(A, B)
        # Call the __call__ method to retrieve the maximum sums
        return [retriver() for _ in range(K)]
