'''
food : 수웅이가 준비한 음식의 양을  / 칼로리가 적은 순서대로 나타내는 정수 배열

이번 대회를 위해 수웅이는 음식을 주문했는데,
대회의 조건을 고려하지 않고 음식을 주문하여 몇 개의 음식은 대회에 사용하지 못하게 되었습니다.

물을 편의상 0번 음식이라고 칭한다

대회를 위한 음식의 배치를 나타내는 문자열을 return 하는 solution 함수 구하기
'''

def solution(food):
    answer = ''
    # 대회에서 1인이 먹을 리스트 food_list에 넣기
    # 0번 음식은 물이기 때문에 1부터 food의 끝까지 범위 설정
    # idx는 음식 번호
    # 대결하는 둘이 같은 양을 먹기 때문에 2로 나눈 몫 만큼 곱해준다.
    person_food = ''
    for idx in range(1, len(food)):
        person_food += str(idx) * (int(food[idx]) // 2)
    # answer 에 person_food + 물인 0 + person_food의 역순으로 나열이 필요
    answer += person_food + '0' + person_food[::-1]

    return answer

print(solution([1, 7, 1, 2]))