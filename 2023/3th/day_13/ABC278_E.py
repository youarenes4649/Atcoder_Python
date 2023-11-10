# pypyで提出

# 入力の受け取り
H,W,N,h,w=map(int,input().split())
# グリッド
G=[]

# g=0~(H-1)
for g in range(H):
    # 入力の受け取り
    Ai=list(map(int,input().split()))
    # グリッドへ追加
    G.append(Ai)

# 初期状態(塗っていない)での各数の出現回数のカウント
Initial=[0]*(N+1)

# g(行)=0~(H-1)
for g in range(H):
    # r(列)=0~(W-1)
    for r in range(W):
        # マス(g,r)の数をカウント
        Initial[G[g][r]]+=1

# 出現回数から種類数を確認
def AnsCount():
    # 種類数
    result=0
    # i=1~N
    for i in range(1,N+1):
        # 出現回数が1以上なら
        if 1<=count[i]:
            # 種類数にカウント
            result+=1
    # 種類数を返す
    return result

# 答え
ans=[[0]*(W-w+1) for i in range(H-h+1)]

# k=0~(H-h)
for k in range(H-h+1):
    # 種類数
    count=[0]*(N+1)
    # i=1~N
    for i in range(1,N+1):
        # 初期値をコピー
        count[i]=Initial[i]

    # (k,0)で塗る場合
    # g(行)=k~(k+h-1)
    for g in range(k,k+h):
        # r(列)=0~(w-1)
        for r in range(w):
            # 塗った部分の数について出現回数をマイナス
            count[G[g][r]]-=1

    # (k,0)の答えを記録
    ans[k][0]=AnsCount()

    # l=1~(W-w)
    for l in range(1,W-w+1):
        # g(行)=k~(k+h-1)
        for g in range(k,k+h):
            # 増えた部分(塗りつぶされなくなった部分)
            count[G[g][l-1]]+=1
            # 減った部分(塗りつぶされた部分)
            count[G[g][l+w-1]]-=1
        # (k,l)の答えを記録
        ans[k][l]=AnsCount()

# i=0~(H-h)
for i in range(H-h+1):
    # 答えの出力(「*」をつけると[]なしで出力)
    print(*ans[i])