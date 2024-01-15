# 240115_

import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

cnt = 0
for i in range(10):
    mario = int(input())
    cnt += mario
    if cnt > 100 :
        if abs(100-cnt) > abs(100-(cnt-mario)):
            print(cnt-mario)
        elif abs(100-cnt) == abs(100-(cnt-mario)):
            print(cnt)
        else:
            print(cnt)
        quit()
else:
    print(cnt)

