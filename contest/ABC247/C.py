N=int(input())

S1='1'
S=['1']
if N==1:
    print(1)
    exit()

for i in range(1,N):
    S.append(S[i-1]+' '+str(i+1)+' '+S[i-1])


print(S[N-1])