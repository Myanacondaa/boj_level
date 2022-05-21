n = list(map(int, input()))

if 0 in n and sum(n)%3 == 0:    # 30의 배수는 3*10의 배수, 각 자리의 합이 3의 배수, 끝 숫자 0
    result = sorted(n, reverse=True)        # 가장 큰 숫자 출력해야 하므로 역정렬
    for num in result:
        print(num, end='')

else:
    print(-1)