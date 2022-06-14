# 순열 이용하기, pypy3에서는 통과
from itertools import permutations
from collections import deque


def insert_operator(x: list[int], q: deque) -> None:
    result = []
    while q:
        op = q.popleft()    # 연산자 튜플
        num = x[0]  # 배열의 맨 처음 값
        for i in range(1, len(x)):
            if op[i-1] == '+':  # 더하기
                num += x[i]
            elif op[i-1] == '-':    # 빼기
                num -= x[i]
            elif op[i-1] == '*':    # 곱하기
                num *= x[i]
            else:   # 나누기
                if num < 0:     # 음수이면 -(|몫|//값)
                    num = -(abs(num)//x[i])
                else:   # 양수이면
                    num //= x[i]

        result.append(num)

    print(max(result))
    print(min(result))


if __name__ == "__main__":
    n = int(input()) # 수의 개수
    arr = list(map(int, input().split()))   # 수 입력
    operator = list(map(int, input().split()))  # 연산가 개수 입력(+,-,*,//)순.
    op_list = ['+', '-', '*', '//']     # 음수일때 나눗셈은 양수로 바꾼 후, (-몫) 형태로
    op = []     # 입력 받은 연산자 개수만큼 기호 추가하기
    for i in range(len(operator)):
        if operator[i] == 0:    # 0개일 때
            continue
        else:
            for j in range(operator[i]):
                op.append(op_list[i])   # 연산자 개수만큼 추가

    op_permu = list(permutations(op))
    insert_operator(arr, deque(op_permu))
