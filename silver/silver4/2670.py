n = int(input())
arr = []
for _ in range(n):
    arr.append(float(input()))

for i in range(1, n-1):
    arr[i] = max(arr[i], arr[i]*arr[i-1])

print('%.3f'%(max(arr)))