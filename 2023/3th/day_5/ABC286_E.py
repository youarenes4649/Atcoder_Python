#直行便をcost1 にしてあげる お土産は負の値にすることで最小値を取らせる
def main():
    INF = 10 ** 20
    N = int(input())
    A = list(map(int,input().split()))
    S = [input() for _ in range(N)]
    cost = [[0,0] * (N + 10) for _ in range(N + 10)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == 'Y':
                cost[i][j] = [1,- A[i]]
            else:
                cost[i][j] = [INF,INF]
    
    #ワーシャルフロイド法 N*N*N の計算量 全点探索のため使用
    for k in range(N): #中間点
        for i in range(N): #始点
            for j in range(N): #終点
                if cost[i][j][0] > cost[i][k][0] + cost[k][j][0]:
                    cost[i][j][0] = cost[i][k][0] + cost[k][j][0]
                    cost[i][j][1] = cost[i][k][1] + cost[k][j][1]
                
                if cost[i][j][0] == cost[i][k][0] + cost[k][j][0]  and cost[i][j][1] > cost[i][k][1] + cost[k][j][1]:
                    cost[i][j][0] = cost[i][k][0] + cost[k][j][0]
                    cost[i][j][1] = cost[i][k][1] + cost[k][j][1]
                
    Q = int(input())
    for _ in range(Q):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        if cost[u][v][0] == INF:
            print('Impossible')
            continue
        print(cost[u][v][0] ,  -(cost[u][v][1] - A[v])  )
        
        
if __name__ == '__main__':
    main()