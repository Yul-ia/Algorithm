import sys
sys.stdin =open('input.txt')
input = sys.stdin.readline

n = int(input())
start = 0

lst = [0,1]

if n == 0:
    print(0)
elif n ==1:
    print(1)
else:
    for i in range(n-1):
        F_num = lst[i]+lst[i+1]
        lst.append(F_num)
    print(F_num)
