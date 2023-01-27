# 理解する
# 
def main():
    from collections import defaultdict
    S = list(map(str,input()))
    S = S[::-1] #逆から見るとやりやすい
    cnt = defaultdict(int)
    ans = 0
    for i in range(len(S)-2):
        cnt[S[i]] += 1
        if S[i] != S[i+1] and S[i+1] == S[i+2]:
            ans += i+1
            ans -= cnt[S[i+1]]# 入れ替える文字と同じものがあったら操作できない
            cnt[S[i+1]] = i+1 # 全ての文字がS[i+1] 文字目に置き換わる 
            S[i] = S[i+1]
            
            
    print(ans)
            
            
        
            
            
            
            
if __name__ == '__main__':
    main()