import math

a, b = map(int, input().split())
n = int(input())
lists = list(map(int, input().split()))
ten = 0	        # 10진법으로 만든 수
result = []
fin = ''

for i in range(n):
    ten += int(lists[i] * math.pow(a, n - i - 1))

while ten:
    nam = ten % b
    result.append(str(nam))
    ten = ten // b

result = result[::-1]
fin = ' '.join(result)
print(fin)