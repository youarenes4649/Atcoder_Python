def main():
    N = int(input())
    cnt = 0
    for s1 in range(1,10):
        for s3 in range(10):
            for s4 in range(10):
                for s5 in range(10):
                    for s7 in range(10):
                        for s8 in range(10):
                            cnt += 1
                            if cnt == N:
                                ans = [str(s1),str(s1),str(s3),str(s4),str(s5),str(s5),str(s7),str(s8),str(s7)]
                                print(''.join(ans))
                                exit()
                                
         
if __name__ == '__main__':
    main()