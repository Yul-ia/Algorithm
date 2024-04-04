# 성 지키기_BOJ1236

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

x, y = map(int, input().split())
dot = []

for _ in range(x):
    dot.append(list(input().strip()))

# 행 접근
r_total =0 # 행 기준 필요한 X수
for p in dot:
    if 'X' not in p:
        r_total +=1


# 열 접급
c_total = 0 # 열 기준 필요한 X수
for i in range(y): #열
    c_cnt = 0 # 열의 X 개수
    for j in range(x): #행
        if dot[j][i] == 'X':
            break
        else:
            c_cnt += 1
    if c_cnt == x: # 한 열에 x가 하나도 없다면
        c_total += 1

print(max(r_total,c_total))
