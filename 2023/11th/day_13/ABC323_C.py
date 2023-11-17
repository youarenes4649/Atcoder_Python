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
    N,M = mi()
    A =li()
    S = []
    for i in range(N):
        s = list(map(str,input()))
        S.append(s)
    now_score = [i for i in range(1,N+1)]
    can_score = [[] for _ in range(N)]

    for i,s_ls in enumerate(S):
        for j,s in enumerate(s_ls):
            if s == 'o':
                now_score[i] += A[j]
            else:
                can_score[i].append(A[j])

    sorted_score =  sorted(now_score)
    max_score = sorted_score[-1]

    for i in range(N):
        i_socre = now_score[i]
        cnt = 0
        if i_socre >= max_score:
            print(0)
            continue
        can_score[i].sort(reverse=True)
        for score in can_score[i]:
            i_socre += score
            cnt += 1
            if i_socre >= max_score:
                print(cnt)
                break

            
    

    
if __name__ == '__main__':
    main()