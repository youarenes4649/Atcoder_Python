import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
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
from collections import defaultdict
def main():
    N = ii()

    cnt = defaultdict(int)
    number = []
    AB = []
    cricle = [False] * (N)
    for _ in range(N):
        a,b = mi()
        number.append(a)
        number.append(b)
        AB.append((a,b))
    number.sort()
    number = set(number)
    UF = UnionFind(len(number))
    zaatu = defaultdict(int)
    for i,n in enumerate(number):
        zaatu[n] = i
        
    for a,b in AB:
        a = zaatu[a]
        b = zaatu[b]
        cnt[a] += 1
        cnt[b] += 1
        if UF.same(a,b) == False:
            UF.merge(a,b)
        else:
            cricle[UF.leader(a)] = True
            
            
    ans = 0
    for group in UF.groups():
        #木ならn - 1 , それ以外ならn
        judge_tree = 0
        check = False
        for i in group:
            judge_tree += cnt[i]
            if cricle[UF.leader(i)]:
                check = True
                break
            
        if check:
            ans += len(group)
            continue
        
        if judge_tree // 2 == len(group) :
            #木の条件
            ans += judge_tree//2 - 1
            
        
            
    print(ans)
            
    
   
        
    
if __name__ == '__main__':
    main()