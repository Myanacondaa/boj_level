n, s = map(int, input().split())
arr = sorted(list(map(int, input().split())))
cnt = 0


def subset_sum(idx, sub_sum):       # 백트래킹
    global cnt
    if idx >= n:
        return
    sub_sum += arr[idx]

    if sub_sum == s:
        cnt += 1

    subset_sum(idx+1, sub_sum)      # 현재 값을 더하는 경우

    subset_sum(idx+1, sub_sum-arr[idx])     # 현재 값을 포함하지 않는 경우


subset_sum(0, 0)
print(cnt)