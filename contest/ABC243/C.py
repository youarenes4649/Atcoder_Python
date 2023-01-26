
from collections import defaultdict
N=int(input())

X=[]
Y=[]
R=defaultdict(list)
L=[]
for i in range(N):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)

S=input()

for i in range(N):
    if S[i]=='R':#最小値を辞書に格納する方法がいまいち
        if not  Y[i] in R:
            R[Y[i]]=X[i]

        else:
            R[Y[i]]=min(R[Y[i]],X[i])#これで一番左側のX座標が格納された
    
    else:#Lの時

        L.append([X[i],Y[i]])


for l in L:
    if not l[1] in R: #Lに格納したY座標はRにはないことがある（RE）
        continue

    if R[l[1]]<l[0]:#右向きのxより左向きのxが大きかったら
        print('Yes')
        exit()

print('No')


        


