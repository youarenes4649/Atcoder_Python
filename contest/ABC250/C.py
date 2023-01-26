N,Q = map(int, input().split())

X = [i for i in range(N+1)]
loc = [i for i in range(N+1)]
#print(X)



for i in range(Q):
    x = int(input())
    if loc[x]<N:
        a = loc[x]
        loc[x] += 1
        loc[X[a+1]] -= 1
        X[a] = X[a+1]
        X[a+1] = x

    else:
        a = loc[x]
        loc[x] -= 1
        loc[X[a-1]] += 1
        X[a] = X[a-1]
        X[a-1] = x


print(*X[1:])

    






