N = int(input())
S = list(map(str,input()))

check=0# 括られたらTrue

for i in range(N):
    if S[i] =='"':
        check=1-check
        continue
    if check == 0:
        if S[i] == ',':
            S[i] = '.'

print(''.join(S))


