S = input()

in_box = set()
box = [[]]

ans = 'Yes'

for i in range(len(S)):
    if S[i] == '(':
        box.append([])
    elif S[i] == ')':
        for c in box[-1]:
            in_box.discard(c)
        box.pop()
    else:
        if S[i] in in_box:
            ans = 'No'
        box[-1].append(S[i])
        in_box.add(S[i])
        print(box)

print(ans)

