# 팰린드롬인지 확인하기 _BOJ10988

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

word = list(input().strip())
N = len(word)

for i in range(N//2+1):
    if word[i] != word[N-1-i]:
        print(0)
        quit()
    elif word[i] == word[N-1-i]:
        pass
print(1)

