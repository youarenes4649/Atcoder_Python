
def main():
    N,L = map(int,input().split())
    ans = []
    for _ in range(N):
        a,b = input().split()
        a = int(a)
        if b =='E':
            ans.append(L-a)
        else:
            ans.append(a)
    
    ans.sort()
    print(ans[-1])
        
if __name__ == '__main__':
    main()