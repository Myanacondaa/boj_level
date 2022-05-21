n, m = map(int, input().split())
arr = []
result = []
for i in range(2):
    arr.append(list(map(int, input().split())))

for i in range(len(arr)):
    for j in range(len(arr[i])):
        result.append(arr[i][j])

for ele in sorted(result):
    print(ele, end= ' ')

