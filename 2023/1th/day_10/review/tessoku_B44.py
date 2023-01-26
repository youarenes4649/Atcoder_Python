
def main():
    N = int(input())
    A = []
    for i in range(N):
        a = list(map(int,input().split()))
        A.append(a)
    Q = int(input())
    gyou = [i for i in range(N)]
    for _ in range(Q):
        q = list(map(int,input().split()))
        if q[0] == 1:
            x,y = q[1:]
            gyou[x-1],gyou[y-1] = gyou[y-1],gyou[x-1]
            
        else:
            x,y = q[1:]
            print(A[gyou[x-1]][y-1])
            
        
if __name__ == '__main__':
    main()