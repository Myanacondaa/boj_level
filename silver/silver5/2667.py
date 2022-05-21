import sys
input = sys.stdin.readline

count = 0

def complex_number(x:list[list[int]], n:int) -> list[int]:
    global count
    result = []
    def dfs(i: int, j: int): # 깊이 우선 탐색
        global count
        if i<0 or j<0 or i>=n or j>=n or x[i][j] != '1':
            # 인덱스 범위 벗어나거나 집이 없는 경우 종료
            return
        x[i][j] = '0' # 한 번 방문한 집은 '0'으로 표시해서 중복 방지
        count += 1 # 집이 있는 곳 한 번 방문할 때마다 개수 추가
        dfs(i-1, j) # 위로
        dfs(i+1, j) # 아래로
        dfs(i, j-1) # 왼쪽
        dfs(i, j+1) # 오른쪽

    for i in range(n):
        for j in range(n):
            if x[i][j] == '1': # 집이 있다면
                dfs(i, j) # 탐색
                result.append(count) # 집 개수 리스트에 추가
                count = 0

    return result



if __name__ == "__main__":
    N = int(input())
    complex_house = []
    for _ in range(N):
        house = list(input())
        house.pop()
        complex_house.append(list(house))

    result = complex_number(complex_house, N)

    print(len(result))
    for ele in sorted(result): # 오름차순 정렬
        print(ele)

