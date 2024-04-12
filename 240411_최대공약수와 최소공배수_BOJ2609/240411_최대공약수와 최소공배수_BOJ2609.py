# 최대공약수와 최소공배수_BOJ2609
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

a,b = map(int,input().split())
tms = a*b

#GCD
if a > b:
  a,b=a,b

while b !=0:
  temp = b
  b = a%b
  a = temp
  # a,b = b,(a%b)

print(a) # 최대공약수
print(tms//a) # 최소공배수