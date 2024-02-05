# 240205_가장 큰 금민수

import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

N = int(input())

for i in range(N,3,-1):
    Num = str(i)
    for j in Num:
        if int(j) != 7 and int(j) != 4:
            break
        else:
            pass
    else:
        print(Num)
        quit()
