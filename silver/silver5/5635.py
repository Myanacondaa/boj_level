n = int(input())
result = []
for _ in range(n):
    name, d, m, y = input().split()
    result.append([name, int(d), int(m), int(y)])

result.sort(key=lambda x: (x[3], x[2], x[1]))

print(result[-1][0])
print(result[0][0])
