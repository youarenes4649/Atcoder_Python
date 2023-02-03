class UnionFind:
    def __init__(self, n):
        self.n=n
        self.parent_size=[-1]*n

    def merge(self, a, b):#a,bを同じグループとして記録
        x, y=self.leader(a), self.leader(b)
        if x == y: return 
        if abs(self.parent_size[x])<abs(self.parent_size[y]): x, y=y, x
        self.parent_size[x] += self.parent_size[y] 
        self.parent_size[y]=x
        return 

    def same(self, a, b):#a,bが同じグループならTrueを返す
        return self.leader(a) == self.leader(b)

    def leader(self, a):#aのリーダー（元の根を返す）
        if self.parent_size[a]<0: return a
        self.parent_size[a]=self.leader(self.parent_size[a])
        return self.parent_size[a]

    def size(self, a):#aが所属しているグループのサイズを返す
        return abs(self.parent_size[self.leader(a)])

    def groups(self):#groupをリストで返す
        result=[[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]

def main():
    N,M,K = map(int,input().split())
    cnt = [0] * N # 直接つながっている数を数える
    uf_frined = UnionFind(N)
    uf_blocked = UnionFind(N)
    for i in range(M):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        uf_frined.merge(a,b)
        cnt[a] += 1
        cnt[b] += 1

    for i in range(K):
        c,d = map(int,input().split())
        c -= 1
        d -= 1
        uf_blocked.merge(c,d)
        if uf_frined.same(c,d):#もし同じ友好関係の連結生分上にいたら
            cnt[c] += 1
            cnt[d] += 1
            
    ans = []
    for i in range(N):
        cand = uf_frined.size(i) - cnt[i] - 1
        ans.append(cand)
        
    print(*ans)
        

if __name__ == '__main__':
    main()