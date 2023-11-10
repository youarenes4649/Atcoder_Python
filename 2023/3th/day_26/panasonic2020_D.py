N = int(input())
al = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
import sys
sys.setrecursionlimit(10**7)

ans = []
def dfs(x,now):#al[now]まで使っていいよ,xは文字列
    if len(x) == N:
        ans.append(x)
        return
    for i in range(now+1):
        if i == now:
            dfs(x+al[i],now+1) #全部違う文字は１回しか生成されない
            return
        dfs(x+al[i],now)

dfs("a",1)

for i in range(len(ans)):
    print(ans[i])