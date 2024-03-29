# 내 학점을 구해줘_BOJ10984
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

t= int(input()) # 학기

for _ in range(t):
    object = int(input()) # 과목수
    c_cnt = 0
    g_cnt = 0
    for _ in range(object):
        c, g = map(float,input().split())
        c_cnt+=c
        g_cnt+= c*g
    print(int(c_cnt),round((g_cnt/c_cnt),1))