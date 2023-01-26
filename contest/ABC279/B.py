S=input()
T=input()

if len(S)<len(T):
    print('No')
    exit()

if S==T:
    print('Yes')
    exit()

for i in range(len(S)-len(T)+1):
    if T==S[i:i+len(T)]:
        print('Yes')
        exit()

print('No')
