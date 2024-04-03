# 더하기 사이클_BOJ1110

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n= input().strip() #26
orgin = int(n) # break조건 확인용
cnt = 0

while True:
    if len(n)<2:
        hap = 0 + orgin
    else:
        hap = int(n[0]) + int(n[1])
    s_hap = str(hap)  # 8
    new = n[-1] + s_hap[-1]  # 68
    cnt += 1

    if int(new) == orgin: # 확인
        break

    n = new

print(cnt)
