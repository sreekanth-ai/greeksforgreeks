class Solution:
    
    #Function to return list of integers that form the boundary 
    #traversal of the matrix in a clockwise manner.
    def BoundaryTraversal(self,matrix, n, m):
        output = []
        
        #base case if number of row or column is 1 then adding all elements.
        if(n == 1):
            i = 0;
            while i < m:
                output.append(matrix[0][i])
                i+=1
        elif(m == 1):
            i = 0;
            while i < n:
                output.append(matrix[i][0])
                i+=1
        else:
            
            #we take care of fact that we don't add any number multiple times.
            
            #traversing first row and adding elements in the list.
            row_ind = 0
            col_ind = 0
            while col_ind < m:
                output.append(matrix[row_ind][col_ind])
                col_ind+=1
    
            #traversing last column and adding elements in the list.
            col_ind = m-1
            row_ind += 1
            while row_ind < n:
                output.append(matrix[row_ind][col_ind])
                row_ind += 1
    
            #traversing last row and adding elements in the list.
            row_ind = n-1
            col_ind -= 1
            while col_ind > -1:
                output.append(matrix[row_ind][col_ind])
                col_ind -= 1
    
            #traversing first column and adding elements in the list.
            col_ind = 0
            row_ind -= 1
            while row_ind > 0:
                output.append(matrix[row_ind][col_ind])
                row_ind -= 1
    
        #returning the list.
        return output
