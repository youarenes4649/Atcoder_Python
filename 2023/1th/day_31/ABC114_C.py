import sys
sys.setrecursionlimit(1000000)
 
def main():
    from collections import deque
    N = int(input())
    if N < 357:
        print(0)
        exit()
    def check(n):
        if '3' in n and '5' in n and '7' in n:
            return True
        
        return False
    def dfs(num):
        for s in [3,5,7]:
            m = 10 * num + s # ここを違う文字にしないとバグつ
            print(m)
            if m <= N:
                if check(str(m)):
                    que.append(m)
                dfs(m)
    
    que = []
    dfs(0)
    print(len(que))
    
    
    
    
    
if __name__ == '__main__':
    main()