import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

a_num = int(input()) # 진짜 약수의 개수

lst = list(map(int,input().split()))


for i in range(a_num):
    mult_lst = []
    for j in range(a_num):
        mult = lst[i]*lst[j]
        mult_lst.append(mult)
    break # 첫번째 list만 담고 멈춰
# print(mult_lst)

m_cnt = []
for p in mult_lst:
    cnt = [] #
    for q in lst:
        if p % q !=0:
            break
        else:
            cnt.append(p)
    if len(cnt) == a_num:
        m_cnt.append(p)
print(min(m_cnt))