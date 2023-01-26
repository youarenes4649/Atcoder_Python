
def main():
    N,K = map(int,input().split())
    S = input()
    if S.count('1') %2 == K % 2 :
        print('Yes')
        
    else:
        print('No')
        
if __name__ == '__main__':
    main()