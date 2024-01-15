# 일곱 난쟁이_BOJ2309

import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

height=[]

for i in range(9):
    h = int(input())
    height.append(h)

height.sort()
total = sum(height)

for j in range(9):
    for k in range(j+1,9):
        if total - (height[j]+height[k])==100:
             for t in range(9):
                 if t == j:
                     pass
                 elif t == k:
                     pass
                 else:
                     print(height[t])
             quit()



