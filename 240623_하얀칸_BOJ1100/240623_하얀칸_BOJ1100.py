# 하얀칸_BOJ1100

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
.  F  .  F  .  .  .  F
흰 검 흰 검  흰 검  흰 검
0 1  2  3   4 5   6  7

F  . . . F . F  .
검 흰 검 흰 검 흰 검 
...'''

cnt = 0

for i in range(1,9):
    line = input().strip()
    for j in range(8):
        # print(line[j])
        if i % 2 !=0 : # 홀수 번째 줄 흰검 start
            if (j==0) and (line[j] == 'F' ):
                cnt +=1
            elif (j % 2 ==0) and (line[j] == 'F'):
                cnt +=1
        else:
            if (j % 2 !=0) and (line[j] == 'F'):
                cnt += 1

print(cnt)