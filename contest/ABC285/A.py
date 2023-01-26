def main():
    a,b = map(int,input().split())
    if b == (2*a) or b == 2*a+1:
        print('Yes')
    else:
        print('No') 
if __name__ == '__main__':
    main()