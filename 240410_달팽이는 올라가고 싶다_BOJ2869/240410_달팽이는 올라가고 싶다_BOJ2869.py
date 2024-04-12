# 달팽이는 올라가고 싶다_BOJ2869

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

s = list(map(int,input().split()))
a,b,v = s[0],s[1],s[2]

if (v-b)%(a-b)==0:
  print(int((v-b)/(a-b)))
else:
  print(int((v-b)/(a-b))+1)