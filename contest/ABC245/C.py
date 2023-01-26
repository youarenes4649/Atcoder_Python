N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

dp=[[False]*2 for _ in range(N)]
cost=[]
for i in range(N):
    cost.append([A[i],B[i]])
dp[0][0]=True
dp[0][1]=True
for i in range(N-1):
    for j in range(2):

        if dp[i][j]==True:   
            if abs(cost[i][j]-cost[i+1][0])<=K:
                dp[i+1][0]=True

            if abs(cost[i][j]-cost[i+1][1])<=K:
                dp[i+1][1]=True

if dp[N-1][0]==True or dp[N-1][1]==True:
    print('Yes')

else:
    print('No')



        
        


    

    


        



        
    
    

    
        




