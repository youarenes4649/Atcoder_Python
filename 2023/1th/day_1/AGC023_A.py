
def main():
    from collections import defaultdict
    from itertools import accumulate
    N = int(input())
    A = list(map(int,input().split()))
    A_cum = list(accumulate(A))
    cnt = defaultdict(int)
    ans = 0
    for i in range(len(A_cum)):
        cnt[A_cum[i]] += 1
        
    ans += cnt[0] #コーナーケース
    for c in cnt:
        ans += cnt[c]*(cnt[c]-1)//2
    
    print(ans)
    
    
        
if __name__ == '__main__':
    main()