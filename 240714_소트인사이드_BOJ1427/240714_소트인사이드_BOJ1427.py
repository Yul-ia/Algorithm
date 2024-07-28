import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

lst = list(map(int,input().strip()))

lst.sort(reverse=True)


print(*lst,sep='')