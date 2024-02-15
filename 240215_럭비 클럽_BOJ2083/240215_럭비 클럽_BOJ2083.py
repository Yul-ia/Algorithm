# 럭비 클럽_BOJ2083

import sys
sys.stdin=open("input.txt")
input = sys.stdin.readline

while True:
    a = input().split()
    if a[0] == "#":
        quit()
    else:
        if int(a[1])>17 or int(a[2])>=80:
            print(a[0],"Senior")
        else:
            print(a[0],"Junior")