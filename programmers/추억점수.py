def solution(name, yearning, photo):
    answer = []
    my_dict = {}
    # name => yearning 키 벨류로 my_dict에 추가
    for n in range(len(name)):
        my_dict[name[n]] = yearning[n]
    # my_dict => {'may': 5, 'kein': 10, 'kain': 1, 'radi': 3}

    
    for i in photo:
        # ["may", "kein", "kain", "radi"]
        count = 0
        # i[idx]가 name에 있는 문자열이면 my_dict의 네임키에 해당하는 점수를 count에 추가
        for idx in range(len(i)):
            if i[idx] in name:
                count += my_dict[i[idx]]
        answer.append(count)

    return answer

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))