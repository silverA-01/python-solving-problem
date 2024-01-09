'''
매일 1명의 가수가 노래를 부르고 점수 부여

매일 출연한 가수의 점수가
지금까지 출연 가수들의 점수 중 상위 k번째 이내이면
해당 가수의 점수를 명예의 전당이라는 목록에 올려 기념합니다.

프로그램 시작 이후 초기에 k일까지는
모든 출연 가수의 점수가 명예의 전당에 오르게 됩니다.

k일 다음부터는
출연 가수의 점수가 기존의 명예의 전당 목록의 k번째 순위의 가수 점수보다 더 높으면,
출연 가수의 점수가 명예의 전당에 오르게 되고
기존의 k번째 순위의 점수는 명예의 전당에서 내려오게 됩니다.

k : 명예의 전당 목록의 점수의 개수

이 프로그램에서는 매일 "명예의 전당"의 최하위 점수를 발표
score : 1일부터 마지막 날까지 출연한 가수들의 점수

매일 발표된 명예의 전당의 최하위 점수를 return하는 solution 함수 구하기
'''

def solution(k, score):
    answer = []
    day_score = []
    for i in range(len(score)):
        # k일까지 day_score에 출연자 점수 추가
        if i < k:
            day_score.append(score[i])
        else:
            # k일 이후부터 출연자 점수가 day_score의 최하점보다 높으면
            # 최하점을 day_score 리스트에서 지우고 출연자 점수를 추가
            if score[i] > min(day_score):
                day_score.remove(min(day_score))
                day_score.append(score[i])
        # for문을 순회할 때마다 day_score의 최하점을 추가
        answer.append(min(day_score))

    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))