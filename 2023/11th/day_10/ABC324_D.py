import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))

def main():
    N = ii()
    S = list(str(ii()))
    square_number_ls = []
    for i in range(10**7):
        so = list(str(i**2))
        so.sort()
        square_number_ls.append(so)


    ans = 0
    S.sort()
    S = ['0'] + S
    if S[-1] == '0':
        print(0)
        exit()

    while S[0] == '0':
        S = S[1:]
        for square in square_number_ls:
            if S== square:
                ans += 1

    print(ans)


   

    


if __name__ == '__main__':
    main()