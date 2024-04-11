# 평균은 넘겠지_BOJ4344
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    ipt = list(map(int,input().split()))
    avg = sum(ipt[1:])/ipt[0]
    cnt=0
    for i in range(1,len(ipt)):
        if ipt[i] > avg:
            cnt +=1
    print(round(cnt/ipt[0]*100,3),"%",sep="")