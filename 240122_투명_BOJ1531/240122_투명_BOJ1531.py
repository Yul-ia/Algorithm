# 240122_투명

import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

N,M= map(int,input().split())

lst2 = []
for i in range(100):
    lst = [0]*100
    lst2.append(lst)

cnt = 0
for j in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for k in range(x1-1,x2):
        for q in range(y1-1,y2):
            lst2[k][q] +=1

for r in range(100):
    for c in range(100):
        if lst2[r][c]>M:
            cnt +=1
print(cnt)

