# Football Team_BOJ5358

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

w = ''
while True:
        s = input()
        if not s:
            break
        for i in s:
            if i == 'i':
                w += 'e'
            elif i == 'e':
                w += 'i'
            elif i == 'I':
                w += 'E'
            elif i == 'E':
                w += 'I'
            else:
                w += i
print(w)