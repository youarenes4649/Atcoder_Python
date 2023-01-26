N,X=map(int,input().split())
S=input()
T=[]
for c in S:
    if c=='U' and len(T)>0 and (T[-1]=='L' or T[-1]=='R'):#これ覚える
        T.pop()
        #これによりT[-1]が排除されるかつUはappendされないからはいらない
    else:
        T.append(c)

for c in T:
    if c=="U": X=X//2
    if c=="L": X=X*2
    if c=="R": X=X*2+1

print(X)

#完全二分木は２進数で表すことでも可能
