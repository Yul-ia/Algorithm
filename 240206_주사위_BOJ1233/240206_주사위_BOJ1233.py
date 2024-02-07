# 주사위_BOJ1233

import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

s1, s2, s3 = map(int, input().split())

lst = []
for i in range(1,s1+1):
    for j in range(1,s2+1):
        for k in range(1,s3+1):
            lst.append(i+j+k)

new_dic = dict()
cnt = 0
for x in lst:
    if x not in new_dic:
        new_dic[x] = lst.count(x) # 딕셔너리에 {x : 빈도수} 로 저장해.

lst3 = []
max_value = max(new_dic.values())
for v in new_dic:
    if new_dic[v] == max_value:
        lst3.append(v)

print(min(lst3))
