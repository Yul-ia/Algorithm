# 쉽게 푸는 문제_BOJ1292
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

a,b = map(int,input().split())
lst =[]

for i in range(b+1):
    s = str(i)
    for j in range(i): #str형태의 s를 i번 쓸 수 있어.
        lst.append(int(s))

cnt = 0
for p in range(a-1,b):
    cnt += lst[p]
print(cnt)
