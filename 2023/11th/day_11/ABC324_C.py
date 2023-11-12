import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))

def check(s,t):
    if len(s) > len(t):
        return check(t,s)
    
    if len(t) - len(s) > 1:
        return False
    
    miss = 0
    l = 0
    r = 0
    while l < len(s):
        if s[l] == t[r]:
            l += 1
            r += 1
        else:
            miss += 1
            if miss > 1:#２回以上ミスったらなし
                return False
            
            if len(s) == len(t): #長さが同じ時は一緒にずらさないと必ずミスが増えてしまう
                l += 1
            r += 1

    return True
            

def main():
    N,T = list(map(input().split()))
    N = int(N)
    S = []
    for i in range(N):
        s = list(map(str,input()))
        S.append(s)

    ans = []
    for i,s in enumerate(S):
        if check(s,T):
            ans.append(i+1)

    print(len(ans))
    print(*ans)

    
if __name__ == '__main__':
    main()