class Solution:
    def fourSum(self, a, k):
        n=len(a)
        ans=[]
        if(n < 4):
            return ans
        a.sort()
        for i in range(0, n-3):
            # current element is greater than k then no quadruplet can be found
            if (a[i] > 0 and a[i] > k):
                break
            # removing duplicates
            if (i > 0 and a[i] == a[i - 1]):
                continue
            
            for j in range(i+1, n-2):
                # removing duplicates
                if (j > i + 1 and a[j] == a[j - 1]):
                    continue
    
                # taking two pointers
                left = j + 1
                right = n - 1
                while (left < right):
                    old_l = left;
                    old_r = right;
                    # calculate current sum
                    sum = a[i] + a[j] + a[left] + a[right]
                    if (sum == k):
                        # add to answer
                        ans.append([a[i], a[j], a[left], a[right]])
    
                        # removing duplicates
                        while (left < right and a[left] == a[old_l]):
                            left+=1
                        while (left < right and a[right] == a[old_r]):
                            right-=1
                    elif (sum > k):
                        right-=1
                    else:
                        left+=1
                    
        return ans;
