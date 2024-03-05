# Goodbye,Code Jam_BOJ29738

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

t =int(input())

for i in range(1,t+1):
    n = int(input())  # 마지막 라운드 등수
    if n < 26:
        print(f"Case #{i}: World Finals")
    elif n < 1001:
        print(f"Case #{i}: Round 3")
    elif n < 4501:
        print(f"Case #{i}: Round 2")
    else:
        print(f"Case #{i}: Round 1")
