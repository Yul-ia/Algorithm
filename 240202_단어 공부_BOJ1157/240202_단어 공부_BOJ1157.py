# 단어공부 _BOJ1157

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

word = input().strip().upper()

cnt_lst=dict()
for i in range(len(word)):
    s = word[i] # s에 저장
    cnt = 0
    if s not in cnt_lst:
        # cnt = word.count(s)
        for j in range(len(word)):
            if s == word[j]:
                cnt += 1
        cnt_lst[s] = cnt

max_count = max(cnt_lst.values())
if list(cnt_lst.values()).count(max_count) >=2:
    print('?')
else:
    for k in cnt_lst:
        if cnt_lst[k] == max_count:
            print(k)
