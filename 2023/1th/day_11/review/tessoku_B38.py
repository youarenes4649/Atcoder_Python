
def main():
    N = int(input())
    S = input()
    kusa = [1]*(N)
    for i in range(N-1):
        if S[i] == 'A':
            kusa[i+1] = kusa[i] + 1
  
    for i in range(N-1,0,-1):
        if S[i-1] == 'B':
            kusa[i-1] = kusa[i] + 1
           
    print(sum(kusa))
        
        
if __name__ == '__main__':
    main()