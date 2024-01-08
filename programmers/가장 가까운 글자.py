def solution(s):
    answer = []
    check_str = []
    for idx in range(len(s)):
        # 처음 나온 문자열이면 -1로 표현
        if s[idx] not in check_str:
            answer.append(-1)
        else:

            # 같은 문자열이 여러 개일 때 가까운 것을 고르는 조건 넣기
            # check_str 에서 뒤에서 부터 확인하면 되지 않을까?
            # check_str[::-1] 역순에서 문자열이 처음 나오는 인덱스 + 1 (0부터 시작이니까)이
            # 같은 문자열이 앞에 몇칸 있는지 구하는 값
            answer.append(check_str[::-1].index(s[idx]) + 1)
        # 처음 나온지 확인용 리스트라 순회 후 요소 추가
        check_str.append(s[idx])

    return answer

print(solution("foobar"))