# 240126_종이자르기

import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

a,b = map(int,input().split()) # 종이 가로세로 길이

garo = [0]*b
sero = [0]*a


n = int(input()) # 점 선 개수
for i in range(n):
    x,y = map(int,input().split())
    if x == 0 :
        garo[y] = 1
    elif x == 1:
        sero[y] = 1
garo2=[]
tmp = 0
for j in range(b):
    if garo[j]==0:
        tmp += 1
    elif garo[j]==1:
        garo2.append(tmp)
        tmp = 1
else:
    garo2.append(tmp)

# print(garo2)

sero2 = []
tmp2 = 0

for p in range(a):
    if sero[p] == 0:
        tmp2 += 1
    elif sero[p] == 1:
        sero2.append(tmp2)
        tmp2 = 1
else:
    sero2.append(tmp2)
# print(sero2)

print(max(garo2)*max(sero2))












