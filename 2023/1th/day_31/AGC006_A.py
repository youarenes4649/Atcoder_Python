
def main():
    x,y = map(int,input().split())
    botan = 0
    if y == 0:
        if x <= 0:
            print(y - x)
        else:
            x = -x
            print(y - x + 1)
    
    elif y > 0:
        if x > y:
            x = -x
            print(y - x + 1)
        else:#符号違う時
            if x >= 0:
                print(y - x)
            else:
                if -x > y:
                    x = -x
                    print(x - y + 1)
                else:
                    x = -x
                    print(y - x + 1)                

    else:
        if x > y:
            if x < 0:
                x = -x
                print(abs(y) - x + 2)
            else:
                if x > - y:
                    x = -x
                    print(y - x + 1)
                   
                else:
                    print(abs(y) - x + 1)
        else:
            print(y - x)

if __name__ == '__main__':
    main()