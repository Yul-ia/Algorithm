# 240126_직사각형 네개의 합집합의 면적 구하기

import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

lst2=[]
for q in range(100):
    lst=[0]*100
    lst2.append(lst)

cnt=0
for i in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    for j in range(x1-1,x2-1): # 좌표 / 칸 수가 달라.
        for k in range(y1-1,y2-1):
            lst2[j][k] = 1

for p in range(100):
    for q in range(100):
        if lst2[p][q] >= 1:
            cnt+=1

print(cnt)
