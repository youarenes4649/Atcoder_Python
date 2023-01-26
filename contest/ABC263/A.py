A,B,C,D,E=map(int,input().split())
ls=[A,B,C,D,E]
count=[0]*14

for c in ls:
    count[c]+=1

if count.count(3):
    if count.count(2):
        print('Yes')
        exit()

print('No')
