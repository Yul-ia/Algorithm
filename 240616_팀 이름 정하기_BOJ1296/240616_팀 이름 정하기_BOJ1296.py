# 팀 이름 정하기_BOJ1296

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def love_score (name):
    L = name.count("L")
    O = name.count("O")
    V = name.count("V")
    E = name.count("E")
    score = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E))%100
    return score

y_name = input().strip()
n = int(input())

# best_score = dict()
best_score = {'' : 0}

for j in range(n):
    team_name = input().strip()
    new_name = y_name+team_name
    get_score = love_score(new_name)

    if get_score > max(best_score.values()):
        best_score = {team_name : get_score}
    elif get_score == max(best_score.values()):
        best_score[team_name] = get_score

# print(best_score) # 확인
# sorted_dict = dict(sorted(best_score.items()))

keys = sorted(best_score.keys())

# 모두다 0 이라면
if all(value == 0 for value in best_score.values()):
    print(keys[1])
else:
    print(keys[0])

