import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n,j,h = map(int,input().split())

cnt = 0
while True:
    cnt += 1
    j = (j+1)//2
    h = (h+1)//2
    if j == h:
        break
print(cnt)