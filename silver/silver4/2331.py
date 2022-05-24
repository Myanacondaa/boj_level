n, p = map(str, input().split())
p = int(p)
arr = ['0']*(10**3)
arr[0] = n

for i in range(1, len(arr)):
    sum_d = 0
    for j in range(len(arr[i-1])):
        sum_d += int(arr[i-1][j])**p        # 각 자릿수 ^p 의 합
    if str(sum_d) in arr:                   # 배열 안에 같은 수가 있으면
        print(arr.index(str(sum_d)))       # 그 수가 처음으로 나오는 인덱스 출력(=길이).
        break

    else:
        arr[i] = str(sum_d)                 # 중복된 수가 없을 경우 다음 배열에 문자열로 저장
