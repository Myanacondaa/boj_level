import sys
sys.setrecursionlimit(10**6)

n = int(input())
video = []
for _ in range(n):
    col = list(map(int, input()))
    video.append(col)


def zip_video_with_quad_tree(arr: list[list[int]]):
    sum_ele = 0              # 행렬의 합
    for ele in arr:
        sum_ele += sum(ele)  # 각 행의 원소 합을 더함

    if sum_ele == 0:        # 행렬의 합이 모두 0이면 모든 원소는 0
        print("0", end ='')        # 0 출력 후 종료
        return

    elif sum_ele == len(arr)**2:      # 행렬의 합이 행렬의 넓이와 같으면 모든 원소는 1
        print("1", end ='')        # 1을 출력 후 종료
        return

    print("(", end='')
    for i in range(4):
        section = []
        if i == 0:
            for j in range(len(arr)//2):        # 1/4 구역 슬라이싱 후 section 리스트에 추가
                section.append(arr[j][:len(arr)//2])
            zip_video_with_quad_tree(section)       # 1/4 구역 재귀 호출 후 압축

        elif i == 1:
            for j in range(len(arr)//2):        # 2/4 구역 슬라이싱 후 section 리스트에 추가
                section.append(arr[j][len(arr)//2:])
            zip_video_with_quad_tree(section)       # 2/4 구역 재귀 호출 후 압축
        elif i == 2:
            for j in range(len(arr)//2):         # 3/4 구역 슬라이싱 후 section 리스트에 추가
                section.append(arr[j+(len(arr)//2)][:len(arr)//2])
            zip_video_with_quad_tree(section)       # 3/4 구역 재귀 호출 후 압축
        else:
            for j in range(len(arr)//2):         # 4/4 구역 슬라이싱 후 section 리스트에 추가
                section.append(arr[j+(len(arr)//2)][len(arr)//2:])
            zip_video_with_quad_tree(section)       # 4/4 구역 재귀 호출 후 압축

    print(")", end='')


zip_video_with_quad_tree(video)


