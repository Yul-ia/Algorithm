# 진주로가자_BOJ31009
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n= int(input())
charge =[] # 요금들 저장. 비교위함.
ver = 0 # 진주요금

for _ in range(n):
    d,c = list(map(str,input().split()))
    charge.append(int(c))
    if d =="jinju":
        ver += int(c)

cnt =0 #진주 요금보다 큰 거 저장
for j in charge:
    if j > ver:
        cnt += 1

print(ver)
print(cnt)
