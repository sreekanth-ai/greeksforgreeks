class Solution{
public:
    int equalPartition(int N, int arr[])
    {
        int sum=0;
        for(int i=0;i<N;i++)
          sum+=arr[i];
        if(sum&1)
          return false;
        else
          return issubsetsum(N,arr,sum/2);
    }
    bool issubsetsum(int N,int arr[],int sum)
    {
        vector<vector<bool>> dp(N+1,vector<bool> (sum+1));
        for(int i=0;i<=N;i++)
          dp[i][0]=true;
        for(int i=1;i<=sum;i++)
          dp[0][i]=false;
        for(int i=1;i<=N;i++)
        {
            for(int j=1;j<=sum;j++)
            {
                if(j>=arr[i-1])
                  dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]];
                else
                  dp[i][j]=dp[i-1][j];
            }
        }
        return dp[N][sum];
    }
};
