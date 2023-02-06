from bisect import bisect_left,bisect_right
A,B,Q = map(int,input().split())
s = [int(input())for _ in range(A)]
t = [int(input())for _ in range(B)]
for i in range(Q):
    x = int(input())
    sx = min(A-1,bisect_left(s,x))
    tx = min(B-1,bisect_left(t,x))
    d1 = abs(s[sx-1]-x)+min(abs(t[tx-1]-s[sx-1]),abs(t[tx]-s[sx-1]))#西社から
    d2 = abs(s[sx]-x)+min(abs(t[tx-1]-s[sx]),abs(t[tx]-s[sx]))
    d3 = abs(t[tx-1]-x)+min(abs(s[sx-1]-t[tx-1]),abs(s[sx]-t[tx-1]))
    d4 = abs(t[tx]-x)+min(abs(s[sx-1]-t[tx]),abs(s[sx]-t[tx]))
    print(min(d1,d2,d3,d4))