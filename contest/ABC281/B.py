S=input()
moji1=S[0]
moji2=S[-1]
moji_m=S[1:-1]
cnt=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
cnt_moji=0
for i in range(len(S)):
    if S[i] in cnt:
        cnt_moji+=1
if len(S)!=8:
    print('No')
    exit()
if cnt_moji!=2:
    print('No')
    exit()
if len(moji_m)!=6:
    print('No')
    exit()
if moji1 in cnt and moji2 in cnt:
    if 100000<=int(moji_m)<=999999:
        print('Yes')
        exit()

print('No')


