# 2033년 밈 투표_BOJ29731

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
s =["Never gonna give you up",
"Never gonna let you down",
"Never gonna run around and desert you",
"Never gonna make you cry",
"Never gonna say goodbye",
"Never gonna tell a lie and hurt you",
"Never gonna stop"]

for _ in range(n):
    t = input().strip()
    if t not in s:
        print("Yes")
        quit()
    else:
        continue
print("No")

