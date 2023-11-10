import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
from collections import defaultdict
def main():
    N,M = mi()
    amari = defaultdict(int)
    if 10 ** N < M:
        print(0)
        exit()
    loop_cnt = 0 #ループの周期
    for i in range(1,10000+1):
        now_num = str((10 ** i) // M)
        number = int(now_num[-1])
        if amari[number] == 0:
            amari[number] = i
        else:#既に登場していたら
            loop_cnt = i - amari[number]
            break
    now_idx = i - 1
    loop_number = now_num[:-1]
    N -= now_idx - len(loop_number)
    n_amari = N % len(loop_number)
    ans_num = ''
    for i in range(N // len(loop_number)):
        ans_num += loop_number
        
    ans_num += loop_number[:n_amari]
    print(int(ans_num)%M)  
    
            
            
if __name__ == '__main__':
    main()