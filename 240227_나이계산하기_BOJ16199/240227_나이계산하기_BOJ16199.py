# BOJ16199_나이계산하기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

y1, m1, d1 = map(int,input().split())
y2, m2, d2 = map(int,input().split())

y_age = y2-y1 # 연 나이

# 만 나이
if m1>m2:
    print(y_age-1) # 생일 안 지난 만 나이.
elif m1 == m2 and d1>d2:
    print(y_age - 1)
else:
    print(y_age) # 생일 지난 만 나이

# 세는 나이
print(y_age+1)

# 연 나이
print(y_age)

'''
2000 04 04
2001 03 04

2000 04 04
2001 04 03
'''