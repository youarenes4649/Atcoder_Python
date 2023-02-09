import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353


def main():
    N,A,B = mi()
    if A <= B :
        print(N + 1 - A)
    else:
        ans = B * (N//A) 
        ans -= max(B - ((N % A) + 1) ,0)
        print(ans)
        
    
if __name__ == '__main__':
    main()