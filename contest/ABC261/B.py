N=int(input())
A=[]
for i in range(N):
    a=list(map(str,input()))
    A.append(a)


for i in range(N-1):
    for j in range(i+1,N):
        if A[i][j]=='W':
            if A[j][i]=='W' or A[j][i]=='D':
                print('incorrect')
                exit()

        if A[i][j]=='L':
            if A[j][i]=='L' or A[j][i]=='D':
                print('incorrect')
                exit()
        if A[i][j]=='D':
            if A[j][i]=='W' or A[j][i]=='L':
                print('incorrect')
                exit()

print('correct')