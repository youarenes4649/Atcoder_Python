
def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        s1 = input()
        s2 = input()
        s3 = input()
        
        ans = '0' * N  + '1' * N + '0'
        print(ans)
if __name__ == '__main__':
    main()