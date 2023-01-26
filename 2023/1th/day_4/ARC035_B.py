
def main():
    from collections import defaultdict
    from itertools import accumulate
    mod = 10**9 + 7
    N = int(input())
    T = []
    cnt = defaultdict(int)
    for _ in range(N):
        t = int(input())
        cnt[t] += 1
        T.append(t)
    T.sort()
    T_cum = list(accumulate(T))
    ans = sum(T_cum)
    ans_total = 1
    for i in range(N):
        ans_total *= cnt[T[i]]
        ans_total %= mod
        cnt[T[i]] -= 1
    print(ans)
    print(ans_total)
        
    
    
if __name__ == '__main__':
    main()