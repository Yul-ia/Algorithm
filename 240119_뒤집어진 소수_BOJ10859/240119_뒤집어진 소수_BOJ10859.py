# 240119_뒤집어진 소수

import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

N = input() #str
if N == '1':
    print('no')
    quit()


for q in range(2,int(N)+1):
    if q**2 > int(N):
        break
    if int(N) % q == 0:
        print('no')
        quit()

rN = ''
for i in N:
    if i == '6' :
        rN = '9' + rN
    elif i == '9':
        rN = '6' + rN
    elif i == '3' or i=='4'or i=='7':
        print('no')
        quit()
    else:
        rN = i + rN


rN = int(rN)

for j in range(2,rN+1):
    if j**2 > rN:
        break
    if rN % j == 0:
        print('no')
        quit()
print('yes')
