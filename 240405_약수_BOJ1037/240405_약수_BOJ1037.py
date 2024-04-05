import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

a_num = int(input()) # 진짜 약수의 개수
lst = list(map(int,input().split())) #약수 들

#########case1
for i in range(a_num):
    mult_lst =[] # 모든 약수들의 최소공배수는 이 mult_lst에 반드시 존재
    for j in range(a_num):
        mult = lst[i]*lst[j]
        mult_lst.append(mult)
    break # 첫번째 list만 담고 멈춰

# print(mult_lst)

m_cnt = []
for p in mult_lst: #[9, 12, 6, 36, 18, 24]
    cnt = 0
    for q in lst:
        if p % q !=0:
            break
        else:
            cnt +=1 # p가 q의 배수라면 +1
    if cnt == a_num: # p가 lst 각 원소에 모두 나누어 떨어진다면 = p는 lst의 공배수
        m_cnt.append(p) #lst의 공배수라면 리스트에 넣어
print(min(m_cnt)) #최소 공배수 찾아

#########case2
# print(min(lst)*max(lst))