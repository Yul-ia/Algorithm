# 240205_분해합

import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

N = int(input().strip()) # 분해합

for i in range(10**6):
    tmp = i # M
    for j in str(i):
        tmp = tmp + int(j)
    if tmp == N :
        print(i)
        quit()
else:
    print(0)

