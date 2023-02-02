
def main():
    N,M = map(int,input().split())
    mod = 10 ** 9 + 7
    if abs(N - M) > 1:
        print(0)
        
if __name__ == '__main__':
    main()