'''
해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다.
players : 선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열
callings : 해설진이 부른 이름을 담은 문자열 배열

경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수 구하기
'''

def solution(players, callings):
    answer = []
    '''
    아래와 같이 풀이하니 시간초과로 틀렸음
    for calling in callings:
        for i in range(len(players)):
            if calling == players[i]:
                players.insert(i - 1, players.pop(i))
    '''
    '''
    이 풀이도 시간초과
    callings의 for구문 순회도 시간초과인 것 같다
    
    # for 구문으로 players의 인덱스를 순회하지 않고
    # 해설진이 호출한 선수들의 현재 idx만 있으면 풀 수 있다.
    for calling in callings:
        # players에서 calling에 해당하는 idx값 찾기
        calling_idx = players.index(calling)
        players.insert(calling_idx - 1, players.pop(calling_idx))
    '''
    # 중복을 줄이기 위해 set 활용
    set_callings = set(callings)
    # 호출된 player의 처음 인덱스값만 구해서 호출된 횟수 count를 이용한다.
    for set_calling in set_callings:
        calling_idx = players.index(set_calling)
        count = callings.count(set_calling)
        pop_calling = players.pop(calling_idx)
        players.insert(calling_idx - count, pop_calling)
    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))