# 240115_2017 연세대학교 프로그래밍 경시대회

import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

result = 0
N = int(input())
for i in range(1,N-1):
    for j in range(1,N-1):
        for k in range(1,N-1):
            if i + j + k == N :
                if k >= (j+2):
                    if i%2 == 0:
                        result += 1
print(result)

