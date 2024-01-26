# 240119_색종이

import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

lst2 = []
count =0

for i in range(100):
    lst = [0]*100
    lst2.append(lst)


N = int(input())
for j in range(N):
    x,y = map(int,input().split())
    for k in range(x,x+10):
        for q in range(y,y+10):
            lst2[k][q] = 1


for xx in range(100):
    for yy in range(100):
        if lst2[xx][yy] ==1:
            count +=1

print(count)