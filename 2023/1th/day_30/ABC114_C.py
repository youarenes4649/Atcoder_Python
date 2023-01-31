
def main():
    from collections import deque
    N = int(input())
    if N < 357:
        print(0)
        exit()
    def dfs(num):
        num = str(num)
        
        for s in ['3','5','7']:
            num += s
            if len(num) <= len(str(N)):
                num = int(num)
                if num <= N:
                    que.append(num)
                dfs(num)
    
    que = []
    one = ''
    dfs(one)
    print(len(que))
    
    
    
    
    
if __name__ == '__main__':
    main()