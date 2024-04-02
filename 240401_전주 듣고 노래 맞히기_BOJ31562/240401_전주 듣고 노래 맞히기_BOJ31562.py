# 전주 듣고 노래 맞히기_BOJ31562
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n,m = map(int,input().split()) #정환이 알고 있는 노래, 시도

dic ={}
for _ in range(n):
    inp =list(input().split())
    new_s =''
    for i in inp[2:5]:
        new_s += i
    dic[inp[1]] = new_s

for _ in range(m):
    h = ''
    a,b,c=input().split()
    h+=a+b+c

    lst = []
    cnt = 0
    for j in dic:
        if h == dic[j]:
            cnt +=1
            lst.append(j)
    if cnt == 1:
        print(*lst)
    elif cnt > 1:
        print("?")
    else:
        print("!")