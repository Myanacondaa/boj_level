a, b = map(int, input().split())
arr = []
for i in range(1, b+1):
    for j in range(i):
        arr.append(i)

print(sum(arr[a-1:b]))      # 맨처음을 1번째라고 함.
