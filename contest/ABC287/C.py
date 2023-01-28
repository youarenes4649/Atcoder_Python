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
    N,M = map(int,input().split())
    UF = UnionFind(N)
    if M == 0:
        print('No')
        exit()
    for i in range(M):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        if UF.leader(u) == UF.leader(v):
            print('No')
            exit()
        UF.merge(u,v)
    if len(UF.groups()) != 1:
        print('No')
    print('Yes')
    
    
    
if __name__ == '__main__':
    main()