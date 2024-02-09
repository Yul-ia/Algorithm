# 과제 안 내신분 BOJ5597

import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

lst=[]
for _ in range(28):
    n = int(input())
    lst.append(n)
lst.sort()
# print(lst)

cnt = 0
lst2 = [] # 제출안한 명단
for i in range(28):
    if i != lst[i]-1-(cnt): # 빈자리 채워서 비교.
        lst2.append(lst[i] - 1)
        cnt += 1

#(1,28) 출석이 다 들어 온 경우 / 학생은 30명
if len(lst2) == 0:
    lst2 = [29, 30]
elif len(lst2) == 1:
    if 29 not in lst:
        lst2.append(29)
    else:
        lst2.append(30)
lst2.sort()

print(lst2[0])
print(lst2[1])