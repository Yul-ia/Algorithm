# Gum Gum for Jay Jay_BOJ26489

import sys
sys.stdin = open('input.txt')
# input = sys.stdin.readline

cnt = 0
while True:
    try:
        s = input().strip()
        cnt += 1
    except:
        break
print(cnt)