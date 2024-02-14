# 인공지능 시계_BOJ2530
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

a,b,c = map(int,input().split()) # 현재시간, 분, 초
s = int(input()) #필요한 초

if c+s>=60:
    seplus = (c+s)%60 # 최종 초
    minplus = b+(c+s)//60 # 초에서 더한 분
    if minplus >=60:
        minplus2 = minplus%60 # 최종 분
        a = minplus//60+a # 시간a 업뎃.
        if a>=24:
            print(a%24,minplus2,seplus)
        else:
            print(a, minplus2, seplus)
    else: # minplus가 60보다 작다면
        print(a, minplus,seplus)
else:
    print(a,b,c+s)