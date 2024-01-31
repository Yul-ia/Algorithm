# 최댓값_BOJ2566

import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

lst=[]
for _ in range(9):
    row = list(map(int, input().split()))
    lst.append(row)
big = -1
for i in range(9):
    for j in range(9):
        if lst[i][j] > big:
            big = lst[i][j]
            m_row = i +1
            m_col = j +1
print(big)
print(m_row,m_col)
