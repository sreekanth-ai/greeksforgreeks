class Solution
{
    public:
    //Function to find position of first set bit in the given number.
    unsigned int getFirstSetBit(int n)
    {
        int pos=1;
        while(n > 0) {
            // Checking if last bit is set
            if(n&1){
              return pos;
            }
            
            // Increment position and right shift number
            pos++;
            n=n>>1;
        }
        return 0;
    }
};
