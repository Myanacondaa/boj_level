'''
'나머지 지수승' 사용
a^b mod c를 구하는 방법 (이산수학 p295)
0) b^(k+1) mod m = b * (b^k mod m) mod m
1) a^b mod c에서, b를 이진수로 표현, b를 거꾸로 뒤집기
2) 거꾸로 된 b의 진수마다 b^(2^j) mod c를 구함
3) expo[i] =1이면 x의 현재 값에 b^(2^j) mod c값을 곱한 뒤 나머지 실행
시간 복잡도 : O( (log m)^2 * log n )
'''

a, b, c = map(int, input().split())

expo = format(b, 'b')   #문자열 타입, 이진수로 변환하기


def multi(a: int, expo:str, c: int) -> int:  # 나눠지는 수, 지수를 이진수로 변환한 것, 나누는 수
    power = a % c       # a mod c
    x = 1               # 3) 과정을 저장하는 값
    for i in range(len(expo)):
        if expo[i] == '1':
             x = (x*power) % c
        power = power**2 % c
    return x

print(multi(a, expo[::-1], c))