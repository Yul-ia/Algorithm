import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int,input().split()))
lst.sort(reverse=True)

cnt = 0
for i in range(n):
    tree = lst[i] + i + 1
    if tree > cnt:
        cnt = tree
print(cnt + 1)