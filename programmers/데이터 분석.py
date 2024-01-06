# data =>  ["코드 번호(code)", "제조일(date)", "최대 수량(maximum)", "현재 수량(remain)"]
'''
data : 정렬한 데이터들이 담긴 이차원 정수 리스트
ext : 어떤 정보를 기준으로 데이터를 뽑아낼지를 의미하는 문자열
val_ext : 뽑아낼 정보의 기준값을 나타내는 정수
sort_by : 정보를 정렬할 기준이 되는 문자열

data에서 ext 값이 val_ext보다 작은 데이터만 뽑은 후,
sort_by에 해당하는 값을 기준으로 오름차순으로 정렬하여 return 하도록 solution 함수 구하기
(단, 조건을 만족하는 데이터는 항상 한 개 이상 존재합니다.)
'''



def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    # ext와 sort_by의 라벨이 되는 데이터를 찾기 위한 리스트 생성
    data_label = ["code", "date", "maximum", "remain"]
    # data에서 ext 값이 val_ext보다 작은 데이터만 뽑기
    ext_data = []
    for i in range(4):
        for idx in range(len(data)):
            if ext == data_label[i] and data[idx][i] < val_ext:
                ext_data.append(data[idx])

    # ext_data를 sort_by에 해당하는 값을 기준으로 오름차순으로 정렬
    for i in range(4):
        for idx in range(len(ext_data)):
            if sort_by == data_label[i]:
                answer = sorted(ext_data, key = lambda x:x[i])
    return answer

print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain"))