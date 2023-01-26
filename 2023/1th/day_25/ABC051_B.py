
def main():
    K,S = map(int,input().split())
    ans = 0
    for x in range(K+1):
        for y in range(K+1):
            if K >= S - x -y >= 0:
                ans += 1
                
    print(ans)
if __name__ == '__main__':
    main()