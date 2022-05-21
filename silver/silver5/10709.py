h, w = map(int, input().split())        # 행, 열 입력
joi = []            # 결과 값
for _ in range(h):          # h(행)번 만큼 반복
    cloud = list(map(str, input()))
    tmp = [-1]*w        # 구름이 다 뜨지 않는 경우로 열 개수만큼 저장
    if 'c' in cloud:    # 열에 구름이 있으면 검사
        for i in range(cloud.index('c'), w):
            if cloud[i] == 'c':     # 해당 위치가 구름이 있으면
                tmp[i] = 0  # 0으로 할당
                continue
            tmp[i] = tmp[i-1]+1     # 구름이 있는 자리부터 1분씩 이동하므로

    joi.append(tmp)

for i in range(h):
    for j in range(w):
        print(joi[i][j], end=' ')
    print()
