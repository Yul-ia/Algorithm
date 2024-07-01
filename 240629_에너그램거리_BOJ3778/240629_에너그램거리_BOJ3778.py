# 애너그램거리 _BOJ3778

import sys
# from collections import Counter
sys.stdin = open('input.txt')
input = sys.stdin.readline


n = int(input())

for num in range(n):
    fst = input().strip()
    sec = input().strip()

    fst_count = [0] * 26 # [ 1 2 3 4 5 6 7 8 9.. ]
    sec_count = [0] * 26

    for i in fst:
        fst_count[ord(i) - ord('a')] += 1 # 방문등록
        # print(ord(i)) # 99
        # print(ord('a')) #97
    # print(fst_count)
    for j in sec:
        sec_count[ord(j) - ord('a')] += 1
    # print(sec_count)

    cnt = 0
    for p in range(26):
        cnt += abs(fst_count[p] - sec_count[p])

    print(f'Case #{num+1}: {cnt}')