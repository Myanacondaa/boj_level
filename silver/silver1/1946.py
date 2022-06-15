import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    # 서류 점수를 기준으로 정렬
    score = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
    cnt = 1
    min_score = score[0][1]
    for i in range(1, n):       # 그리디
        if min_score > score[i][1]:     # 서류 점수가 낮은 사람이 면접 점수가 더 높으면 합격
            min_score = score[i][1]
            cnt += 1

    print(cnt)