
def main():
    N,K = map(int,input().split())
    names = []
    for i in range(N):
        s = input()
        if i>=K:
            continue
        names.append((s,len(s)))
    names.sort()


    for i in range(K):
        print(names[i][0])
if __name__ == '__main__':
    main()