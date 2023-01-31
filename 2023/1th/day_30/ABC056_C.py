def main():
    X = int(input())
    ans = 0
    for i in range(1,X+1):
        if i * (i+1) // 2 < X <= (i+1) * (i+2)//2:
            ans = (i+1) * (i+2) //2 - X
            print(i+1)
            exit()
        
if __name__ == '__main__':
    main()