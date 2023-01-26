
def main():
    def func(g):
        return B*(g-1) + A/(g**0.5)
        
    A,B = map(int,input().split())
    
    ok = 10**18
    ng = 1
    while ok-ng > 10:
        
        c1 = (ng*2 + ok)//3
        c2 = (ng + ok*2)//3
        
        if func(c1) > func(c2): ng = c1
        else: ok = c2
        
    
    ans = []
    for i in range(max(1,ng-100),ok+100):
        ans.append(func(i))
        
    print(min(ans))
if __name__ == '__main__':
    main()