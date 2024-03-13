# 핸드폰 요금_BOJ1267
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input()) # 통화 개수

lst = list(map(int,input().split()))
y = 0 # 영식
m = 0# 민식
for i in lst:
    if i <= 29:
        y += 10
    else:
        if i%30==0:
            y += (i//30)*10+10
        else:
            y += (i//30)*10+10


for j in lst:
    if j <= 59:
        m += 15
    else:
        if j%60==0:
            m += (j//60)*15+15
        else:
            m += (j//60)*15+15

if y<m:
    print("Y",y)
elif y==m:
    print("Y","M",y)
else:
    print("M",m)