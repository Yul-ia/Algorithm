# 바구니 뒤집기_BOJ10811

import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

N, M = map(int,input().split()) # 바구니 1부터N개,  M번

N_lst = [] # 1부터 N까지 순서대로 담겨있어.
for n in range(1, N + 1):
    N_lst.append(n)

for _ in range(M):
    i, j = map(int, input().split()) # i <= j
    new = N_lst.copy()  # i 부터 j 까지 역순으로 담을 리스트
    if i == j:
        pass
    else:
        for x in range(i-1,j):
            new[j + i - x - 2] = N_lst[x]
        N_lst = new.copy()


print(*N_lst)
