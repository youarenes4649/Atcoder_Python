
def main():
    mod = 100
    cnt = [0]*100
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    A_new = []
    for a in A:
        cnt[a%mod] += 1
        if a%mod < 50 and a%mod !=0:
            A_new.append(a)
            
    for a in A_new:
        ans += cnt[100 - a%mod]
    if cnt[0]:
        ans += cnt[0]*(cnt[0]-1)//2
        
    if cnt[50]:
        ans += cnt[50]*(cnt[50]-1)//2
        
    print(ans)
        
    
if __name__ == '__main__':
    main()