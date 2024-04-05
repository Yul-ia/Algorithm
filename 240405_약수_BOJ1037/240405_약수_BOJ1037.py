import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

a_num = int(input()) # 진짜 약수의 개수
lst = list(map(int,input().split())) #약수 들

#########case2
print(min(lst)*max(lst))