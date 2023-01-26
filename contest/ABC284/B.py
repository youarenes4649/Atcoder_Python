
def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        cnt = 0
        for a in A:
            if a%2 == 1:
                cnt += 1
                
        print(cnt)
if __name__ == '__main__':
    main()