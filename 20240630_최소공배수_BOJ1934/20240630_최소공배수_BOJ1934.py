import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
# a,b = map(int,input().split())
# tms = a*b

for i in range(n):
    a, b = map(int, input().split())
    tms = a * b

    # GCD

    # GCD
    if a< b:
        a, b = b, a

    while b != 0:
        temp = b
        b = a % b
        a = temp

    while b != 0:
        temp = b
        b = a % b
        a = temp

    print(tms // a)

#
# #GCD
# if a > b:
#   a,b=a,b
#
# while b !=0:
#   temp = b
#   b = a%b
#   a = temp
#   # a,b = b,(a%b)
#
# # print(a) # 최대공약수
# print(tms//a) # 최소공배수(두수곱/최대공약수)