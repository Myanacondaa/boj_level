
n = int(input())  # 수의 개수
arr = list(map(int, input().split()))  # 수 입력
operator = list(map(int, input().split()))  # 연산자 개수 입력(+,-,*,//)순.

maximum = -1e9      # -10^9
minimum = 1e9     # 10^9


def dfs(depth, result, plus, minus, multi, div):
    global maximum, minimum     # 전역 변수 사용
    if depth == n:              # 입력 받은 모든 배열의 연산이 끝났으면
        maximum = max(result, maximum)
        minimum = min(result, minimum)
        return

    if plus:
        dfs(depth+1, result+arr[depth], plus-1, minus, multi, div)

    if minus:
        dfs(depth+1, result-arr[depth], plus, minus-1, multi, div)

    if multi:
        dfs(depth+1, result*arr[depth], plus, minus, multi-1, div)

    if div:
        dfs(depth+1, int(result/arr[depth]), plus, minus, multi, div-1)


dfs(1, arr[0], operator[0], operator[1], operator[2], operator[3])

print(maximum)
print(minimum)




