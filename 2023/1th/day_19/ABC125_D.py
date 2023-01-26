
def main():
    from copy import deepcopy
    N = int(input())
    A = list(map(int,input().split()))
    A_new = [0]*(N)
    mainasu = 0
    for i in range(N):
        if A[i] <= 0:
            mainasu += 1
            A_new[i] = -A[i]
        else:
            A_new[i] = A[i]
            
    if mainasu % 2 == 0:
        print(sum(A_new))
    else:
        print(sum(A_new),min(A_new))
        print(sum(A_new) - min(A_new))

if __name__ == '__main__':
    main()