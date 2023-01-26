N=int(input())
S=[0]+list(map(int,input().split()))
A=[]
for i in range(N):
    A.append(S[i+1]-S[i])

print(*A)