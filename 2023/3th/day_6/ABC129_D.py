#!/usr/bin/env python3
from bisect import bisect_left
from collections import Counter


dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
inf = 1 << 60


def main():
    H, W = map(int, input().split())
    rows = [[-1, W] for _ in range(H)]
    cols = [[-1, H] for _ in range(W)]
    S = []
    for h in range(H):
        s = input()
        S.append(s)
        for w in range(W):
            if s[w] == "#":
                rows[h].append(w)
                cols[w].append(h)
    for h in range(H):
        rows[h].sort()
    for w in range(W):
        cols[w].sort()
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                continue
            val = 0
            hh = bisect_left(rows[h], w)
            val += rows[h][hh] - rows[h][hh - 1] - 1
            ww = bisect_left(cols[w], h)
            val += cols[w][ww] - cols[w][ww - 1] - 1
            val -= 1
            ans = max(ans, val)
    print(ans)


if __name__ == "__main__":
    main()
