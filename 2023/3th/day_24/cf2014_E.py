import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
 
def main():
    N = ii()
    R = li()
    if N < 3:
        print(0)
        exit()
    L = [R[0]]
    for r in R:
        if L[-1] != r:
            L.append(r)
            
    R = L
    ans = 2
    arr = [R[0]]
    for i in range(len(R) - 2):
        if R[i] < R[i+1] and R[i+1] > R[i+2]:
            ans += 1
            arr.append(R[i+1])
        elif R[i] > R[i+1] and R[i+1] < R[i+2]:
            arr.append(R[i+1])
            ans += 1
    
    print(ans) if ans >= 3 else print(0)
    
            
        
        
if __name__ == '__main__':
    main()