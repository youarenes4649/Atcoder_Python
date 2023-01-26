
def main():
    from collections import defaultdict
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    cnt = defaultdict(int)
    for a in A:
        cnt[a] += 1
        
    for i in range(1,N+1):
        print(M-cnt[i])
    
if __name__ == '__main__':
    main()