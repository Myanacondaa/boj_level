n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]      # 1부터 n까지의 사람 리스트
result = []         # 요세푸스 순열을 담을 리스트
tmp = 0
for i in range(n):
    tmp += k-1
    if tmp >= len(arr):
        tmp %= len(arr)

    result.append(str(arr.pop(tmp)))

print("<", ", ".join(result)[:], ">", sep='')