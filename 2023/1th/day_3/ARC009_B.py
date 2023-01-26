
def main():
    from collections import defaultdict
    B = list(map(int,input().split()))
    now = [i for i in range(10)]
    #変換
    change = defaultdict(int)
    for a,b in zip(now,B):
        change[b] = a
    change2 = defaultdict(int)
    for a,b in zip(now,B):
        change2[a] = b
    N =  int(input())
    A = []
    for i in range(N):
        a = input()
        tmp = ''
        for c in a:
            tmp += str(change[int(c)])
        A.append(int(tmp))
    A.sort()
    for i in range(N):
        ans = ''
        for a in str(A[i]):
            ans += str(change2[int(a)])
        print(ans)
            
if __name__ == '__main__':
    main()