import sys
input = sys.stdin.readline
n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)     # 로프의 길이 역정렬

w = 0           #  로프가 들 수 있는 최대 무게

for i in range(n):
    # 로프가 병렬처리 되면 로프의 개수 * 가장 길이가 짧은 로프의 길이만큼 들 수 있음
    if rope[i]*(i+1) > w:
        w = rope[i]*(i+1)


print(w)