
def main():
    N,K = map(int,input().split())
    if N*2 - 2 > K:
        print('No')
        exit()
    if K % 2 == 1:
        print('No')
    else:
        print('Yes')
    
    
if __name__ == '__main__':
    main()