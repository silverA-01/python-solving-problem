'''
자연수 n이 매개변수로 주어집니다.

n을 x로 나눈 나머지가 1이 되도록 하는
가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요.

답이 항상 존재함은 증명될 수 있습니다.

3 ≤ n ≤ 1,000,000
'''

# n은 3이상의 자연수이기 때문에 answer=2 부터 시작
def solution(n):
    answer = 2
    # n을 answer로 나눴을 때 1이 될 때 까지 answer +=1 반복
    while n % answer != 1:
        answer += 1

    return answer

print(solution(12))