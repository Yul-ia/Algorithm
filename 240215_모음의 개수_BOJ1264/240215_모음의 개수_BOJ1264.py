# 모음의 개수_BOJ1264

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

while True:
    s = input()
    s=s.lower()
    cnt = 0
    for i in s:
        if i == 'a' or i =='e' or i=='i' or i=='o' or i=='u' :
            cnt +=1
        elif i =="#":
            quit()
    print(cnt)

