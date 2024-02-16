import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

s = input()

alpha = 'abcdefghijklmnopqrstuvwxyz'

lst = []
for i in alpha:
    if i in s:
        lst.append(s.count(i))
    else:
        lst.append(0)
print(*lst)