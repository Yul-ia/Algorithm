# 240116_적어도 대부분의 배수

import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

N=list(map(int,input().split()))
N.sort()
small = 1e9

for i in range(3):
    for j in range(i+1, 4):
        for k in range(j+1, 5):
            # print(i,j,k)
            big = N[k]
            while 1:
                if not big % N[i] == 0:
                    big += N[k]
                else :
                    if not big % N[j] == 0:
                       big += N[k]
                    else :
                        if big < small:
                            small = big
                        break
print(small)

