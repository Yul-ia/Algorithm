import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

for i in range(3):
    A = list(map(int, input().split()))
    if A[2] > A[5]:
        s = 60-A[2]+A[5] # 새로 저장된 초
        A[4] = A[4]-1
        if A[1] > A[4]:
            m = 60 - A[1]+A[4] # 새로 저장된 분
            A[3] = A[3]-1
            print(A[3]-A[0],m,s)
        else:
            print(A[3]-A[0],A[4]-A[1],s)
    else:
        if A[1] > A[4]:
            m = 60 - A[1]+A[4] # 새로 저장된 분
            A[3] = A[3]-1
            print(A[3]-A[0],m,A[5]-A[2])
        else:
            print(A[3]-A[0], A[4]-A[1], A[5]-A[2])