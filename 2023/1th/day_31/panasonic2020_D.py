import sys
sys.setrecursionlimit(10**7)
def main():
    N = int(input())
    # N! 通りある
    def dfs(s,mx):
        if len(s) == N:
            print(s)
            
        else:
            for j in range(mx+1):
                c = chr(ord('a') + j) 
                if c in s:
                    dfs(s + c ,mx + 1)
                else:
                    # ex) aab aac  aacは標準形ではない
                    dfs(s + c , mx + 1)
                    break
                
    dfs('a',1)
                
if __name__ == '__main__':
    main()