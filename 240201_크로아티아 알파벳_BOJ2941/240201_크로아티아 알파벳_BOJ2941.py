# 크로아티아 알파벳 _BOJ2941

import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = list(input().strip())
ans = len(word)
cnt = 0
for i in range(len(word) - 2):
    if word[i] + word[i + 1] + word[i + 2] in alpha:
        cnt += 2
        word[i], word[i + 1], word[i + 2] = '0', '0', '0'
for j in range(len(word)-1):
	if word[j]+word[j+1] in alpha:
		cnt += 1
		word[j],word[j+1] = '0','0'
print(ans - cnt)

