# 출석 이벤트 _ BOJ25704
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n =int(input())
price = int(input()) #가격

pay = []

if n >= 5:
    pay.append(price-500)
    if n >= 10:
        pay.append(int(price*0.9))
        if n >= 15:
            pay.append(price-2000)
            if n >= 20:
                pay.append(int(price*0.75))
else:
    pay.append(price)

for i in pay:
    if i <= 0: # i는 할인 된 금액.할인금액이 더 크면 0원
        print(0)
        quit()
else:
    print(min(pay))
