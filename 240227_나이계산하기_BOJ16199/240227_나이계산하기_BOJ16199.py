
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

y1,m1,d1 = map(int,input().split())
y2, m2, d2 = map(int,input().split())
'''
연 나이 = 세는 나이 -1
'''
if d2 > d1:
    d3 = d2 - d1
    if m2> m1 :
        m3 = m2 - m1
    else: # m2<m1
        m3 = 12-m1+m2
else:
    # 31일인 달 30일인달 28,29일달? d1> d2
    d3 = 31-d1+d2
    if m2> m1 :
        m3 = m2 - m1
    else: # m2<m1
        m3 = 12-m1+m2
print(m3,d3)

# 만나이
if y2> y1 and m3>=m1 and d3 >= d1:
    print(y2-y1+1) # 만나이
    print(y2-y1+2) # 세는나이
    print(y2-y1+1)
elif y2>y1 and m3<m1 or d3 < d1:
    print(y3-y1)
    print(y3-y1+1)
    print(y3-y1)
else:
    print(y2-y1) # 생일 안 지난 만
    print(y2-y1+1) # 세는 나이
    print(y2-y1) # 연나이

