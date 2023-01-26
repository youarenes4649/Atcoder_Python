
def main():
    from collections import defaultdict
    N,D = map(int,input().split())
    day = defaultdict(list)
    for i in range(N):
        x,y = map(int,input().split())
        day[x].append(y)
    for x in day:
        day[x].sort()
        
    use=[]
    ans = 0
    for d in range(1,D+1):
        use.extend(day[d])
        print(use)
        use.sort()
        ans += use[-1]
        use.pop()
        print(use)
    print(ans)
    
if __name__ == '__main__':
    main()