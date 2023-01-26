def main():
    N,A,B = map(int,input().split())
    S = []
    for i in range(N):
        s = int(input())
        S.append(s)
    S.sort()
    P = B /(S[-1] - S[0])
    Q = A - (P * sum(S)) / N
    print(P,Q)
if __name__ == '__main__':
    main()