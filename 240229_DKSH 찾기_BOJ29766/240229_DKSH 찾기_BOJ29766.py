# DKSH 찾기 _ BOJ29766
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

lst=input().strip()

cnt = 0

for i in range(len(lst)):
    try:
        if lst[i] == "D":
            if lst[i+1] == "K":
                if lst[i+2] == "S":
                    if lst[i+3] == "H":
                        cnt +=1
    except IndexError:
        pass

print(cnt)