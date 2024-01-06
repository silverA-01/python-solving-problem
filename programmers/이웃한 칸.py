'''
[["blue", "red", "orange", "red"],
["red", "red", "blue", "orange"],
["blue", "orange", "red", "red"], [
"orange", "orange", "red", "blue"]]
board[h][w]와 이웃한 칸들 중 같은 색으로 칠해져 있는 칸의 개수 구하기
'''


def solution(board, h, w):
        # board의 길이
    n = len(board[0])
    # 같은 색으로 색칠된 칸의 개수
    count = 0
    # h와 w의 변화량
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    # 반복문
    for i in range(4):
        # h, w의 좌표
        # h 좌표가 위, 아래, 왼쪽, 오른쪽 칸으로 갔을 때와 w좌표가 위, 아래, 왼쪽, 오른쪽 칸으로 갔을 때 순회
        h_check = h + dh[i]
        w_check = w + dw[i]
        # h, w 좌표가 board의 길이안에 있을 때, 보드에서 선택한 좌표 board[h][w]와 고른 칸에서 위, 아래, 왼쪽, 오른쪽 칸으로 갔을 때 같은 색깔일 경우 count 하나 추가
        if h_check >= 0 and h_check < n and w_check >= 0 and w_check < n:
            if board[h][w] == board[h_check][w_check]:
                count += 1
    return count

print(solution([["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]], 1, 1))