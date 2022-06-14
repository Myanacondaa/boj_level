import sys
sys.setrecursionlimit(10**5)

count = 0

def check_rectangle_area(col: int, row: int, rect: list[list[int]]) -> list[int]:
    global count
    # 직사각형의 구역을 1로, 아닌 곳은 0으로 표기, 그 후 숫자 섬 문제와 동일하게 풀면 됨
    # 행, 열, 직사각형 좌표를 매개변수로 받음
    area = []
    for i in range(col):
        area.append([0]*row)

    for i in range(len(rect)):      # 직사각형 구역 표시, 직사각형 개수만큼 반복
        for j in range(rect[i][1], rect[i][3]):
            for l in range(rect[i][2], rect[i][0]):     # y좌표 줄부터 1로 만들기
                area[l][j] = 1

    result = []

    def dfs(i: int, j: int):
        global count
        if i < 0 or j < 0 or i >= len(area) or j >= len(area[0]) or area[i][j] == 1:
            # 범위를 벗어나거나 1이면 종료
            return
        count += 1
        area[i][j] = 1
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    for i in range(len(area)):
        for j in range(len(area[0])):
            if area[i][j] == 0:
                dfs(i, j)
                result.append(count)
                count = 0
    return result


if __name__ == "__main__":
    m, n, k = map(int, input().split())
    rectangle = []
    for _ in range(k):
        left_x, left_y, right_x, right_y = map(int, input().split())
        # 문제의 (x, y)는 실제 수직선의 좌표와 같음.
        # 이 좌표를 이차원 리스트의 좌표로 바꿀거임.
        # (x, y) -> (m-y, x)로 하면 됨.
        rectangle.append([m-left_y, left_x, m-right_y, right_x])

    result = check_rectangle_area(m, n, rectangle)
    print(len(result))
    for ele in sorted(result):
        print(ele, end=' ')

