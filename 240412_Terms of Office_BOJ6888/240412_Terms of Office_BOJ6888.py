# Terms of Office_BOJ6888
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


x=int(input())
y=int(input())

for i in range(x,y+1,60):
  print("All positions change in year", i)
