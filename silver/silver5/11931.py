import sys
input = sys.stdin.readline
n = int(input())
result = []
for _ in range(n):
    result.append(int(input()))

result.sort(reverse=True)
for ele in sorted(result, reverse=True):
    print(ele)