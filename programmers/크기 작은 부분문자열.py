def solution(t, p):
    answer = 0
    p_len = len(p)
    # slice할 start, end 값 지정
    s = 0
    e = len(p)
    
    # p의 길이로 t를 슬라이스한 문자열 추출 후 t_list에 추가
    t_list = []
    while e <= len(t):
        t_list.append(t[s:e])
        s += 1
        e += 1

    # t_list의 요소를 정수화한 값이 정수화한 p보다 작거나 같으면 count에 1 추가
    count = 0
    for tt in t_list:
        if int(tt) <= int(p):
            count += 1

    return count

print(solution("3141592", "271"))