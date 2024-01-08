'''
원하는 카드 뭉치에서 카드를 순서대로 한 장씩 사용합니다.
한 번 사용한 카드는 다시 사용할 수 없습니다.
카드를 사용하지 않고 다음 카드로 넘어갈 수 없습니다.
기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없습니다.

cards1과 cards2에는 서로 다른 단어만 존재합니다.
'''

def solution(cards1, cards2, goal):
    cards1_idx = 0
    cards2_idx = 0
    check_goal = []
    for goal_word in goal:
        # card1의 idx가 cards1의 길이 미만이고 인덱스에 해당하는 cards1의 단어가 goal의 순회하는 goal_word와 같을 때
        if cards1_idx < len(cards1) and cards1[cards1_idx] == goal_word:
            check_goal.append(cards1[cards1_idx])
            cards1_idx += 1
        else:
            # card2rk 위 1가 같은 조건일 때
            if cards2_idx < len(cards2) and cards2[cards2_idx] == goal_word:
                check_goal.append(cards2[cards2_idx])
                cards2_idx += 1

    # 순회가 다 되고 순서대로 넣은 check_goal이 실제로 goal과 같을 때
    if check_goal == goal:
        answer = 'Yes'
        
    # 그렇지 않을 때
    else:
        answer = 'No'
    return answer

print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))