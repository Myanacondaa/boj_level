import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    level = 0

    # 맨 앞과 맨뒤의 차이도 최소화가 되어야 하므로 인덱스의 차이를 2로 두는 것이 좋다
    for i in range(2, n):
        level = max(level, abs(arr[i]-arr[i-2]))

    print(level)

