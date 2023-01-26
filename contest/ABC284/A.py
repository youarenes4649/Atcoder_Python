
def main():
    N = int(input())
    S =[]
    for i in range(N):
        s = input()
        S.append(s)
        
    for s in S[::-1]:
        print(s)
if __name__ == '__main__':
    main()