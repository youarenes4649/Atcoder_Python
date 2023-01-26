#最小全域木　問題を復習
#全域木とは全ての頂点が変異よって連結している木
#最小全域木とは変の重みの総和が最小になるとき
#これを求めるのにプリム法とクラスカル法というものがある
def main():
    N,M = map(int,input().split())
    #どれだけCが正の辺を取り除けるか
    edge = [[]*N for _ in range(N)]
    sum_c = 0
    for _ in range(M):
        a,b,c = map(int,input().split())
    
        edge[a-1].append([b-1,max(c,0)])
        edge[b-1].append([a-1,max(c,0)])
        if c >0:
            sum_c += c
    
    import heapq
    # プリム法
    # 頂点がマークされているか確認する配列
    marked = [False for _ in range(N)]

    # マークされている頂点数を数える
    marked_cnt = 0

    # はじめに0頂点をマーク
    marked[0] = True
    marked_cnt += 1

    # heap
    q = []

    # 頂点0に隣接する辺を保存
    for j, c in edge[0]:
        heapq.heappush(q, (c, j))

    total = 0

    # すべての頂点をマークするまでwhileループ
    while marked_cnt < N:
        # 最小の重みの辺をheapで取り出す
        c, i = heapq.heappop(q)

        # マークされているならスキップ
        if marked[i]:
            continue

        # 頂点をマーク
        marked[i] = True
        marked_cnt += 1

        total += c

        # 頂点iに隣接する辺を保存
        for j, c in edge[i]:
            # マークされていればスキップ
            if marked[j]:
                continue

            heapq.heappush(q, (c, j))

    print(sum_c-total)

    

if __name__ == '__main__':
    main()