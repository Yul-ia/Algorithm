
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

y1,m1,d1 = map(int,input().split())
y2, m2, d2 = map(int,input().split())
'''
연 나이 = 세는 나이 -1
'''
y_age = y2-y1 # 연 나이
# 만 나이
if m1>m2 and d1>d2:
    print(y_age-1)
else:
    print(y_age)

# 세는 나이
print((y_age+1)

# 연 나이
print(y_age)