
def main():
    from collections import defaultdict
    N = int(input())
    A = list(map(int,input().split()))
    cnt = defaultdict(int)
    for a in A:
        cnt[a] += 1
    ans = 0
    for c in cnt:
        print(c)
        if cnt[c] >=3:
            ans += cnt[c]*(cnt[c]-1)*(cnt[c]-2)//(3*2*1)
    print(ans)
            
    
if __name__ == '__main__':
    main()