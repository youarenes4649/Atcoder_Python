S=input()

len_s=len(S)

if len_s==1:
    tmp=S
    for i in range(5):
        S+=tmp
        

    print(S)

elif len_s==2:
    tmp=S
    for i in range(2):
        S+=tmp
        

    print(S)

else:
    tmp=S
    for i in range(1):
        S+=tmp
        

    print(S)