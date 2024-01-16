# 240116_방 배정 정하기

import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

N=list(map(int,input().split()))


for x in range(N[3]//N[0] + 1):
    for y in range(N[3]//N[1]+1):
        for z in range(N[3]//N[2]+1):
            if N[0]*x + N[1]*y + N[2]*z == N[3]:
                print(1)
                quit()
else:
    print(0)

