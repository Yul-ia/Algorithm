# Welcome to SMUOCP!_BOJ29699

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

w ="WelcomeToSMUPC"
n= int(input())
w = w*(n//10+1)

print(w[n-1])