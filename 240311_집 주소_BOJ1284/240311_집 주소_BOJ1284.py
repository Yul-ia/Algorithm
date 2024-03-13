# 집 주소_BOJ1284

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

while True:
    n = input().strip()
    cnt =0
    if int(n)==0:
        break
    else:
        for i in n:
            if int(i) ==1:
                cnt += 2
            elif int(i) ==0:
                cnt +=4
            else:
                cnt +=3
        print(cnt+2+len(n)-1)
