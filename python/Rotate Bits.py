class Solution:
    def rotate(self, n, d):
        d = d % 16
        res = [0, 0]
        
        # Storing n in a temporary variable
        temp = n
        
        mask = (1 << d) - 1  # Picking up the leftmost d bits
        shift = (temp & mask)
        temp = (temp >> d)  # Moving the remaining bits to their new location
        temp += (shift << (16 - d))  # Adding removed bits at the rightmost end
        res[1] = temp  # Storing the new number
    
        temp = n
        mask = ~((1 << (16 - d)) - 1)  # Picking the rightmost d bits
        shift = (temp & mask)
        temp = (temp << d)  # Moving the remaining bits to their new location
        temp += (shift >> (16 - d))  # Adding removed bits at the leftmost end
        res[0] = temp  # Storing the new number
    
        mask = (1 << 16) - 1
        res[0] = (res[0] & mask)
        
        return res
