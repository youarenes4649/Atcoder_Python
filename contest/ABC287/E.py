def check(S,T):
    cnt = 0
    for i in range(min(len(T),len(S))):
        if S[i] == T[i]:
            cnt += 1
        else:
            return cnt
    
    return cnt
            
N = int(input())
S = [(input(),i) for i in range(N)]
S.sort()

ans = [0]*N
for i in range(N):
    if i == 0:
        ans[S[i][1]] = check(S[i][0],S[i+1][0])
    elif i == N - 1:
        ans[S[i][1]] = check(S[i][0],S[i-1][0])
    else:
        ans[S[i][1]] = max(check(S[i][0],S[i+1][0]),check(S[i][0],S[i-1][0]))
        
for a in ans:
    print(a)
