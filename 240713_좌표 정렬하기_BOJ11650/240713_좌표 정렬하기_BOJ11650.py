import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

lst = []

for i in range(n):

   x,y = map(int,input().split())
   lst.append((x,y))

lst.sort(key=lambda x:(x[0],x[1]))
for x, y in lst:
    print(x, y)

