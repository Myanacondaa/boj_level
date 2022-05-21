n = int(input())
result = []
for _ in range(n):
    result.append(float(input()))

result.sort()
for i in range(7):
    print(f'{result[i]:.3f}')