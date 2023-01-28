
def main():
    N = int(input())
    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        s = input()
        if s == 'For':
            cnt1 += 1
            
        else:
            cnt2 += 1
            
    if cnt1>cnt2:
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    main()