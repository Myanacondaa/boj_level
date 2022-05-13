def change(x: list[int], num:int):
    if x[num] == 0: # 0이면 1로 바꿈
        x[num] = 1
    else: # 1이면 0으로 바꿈
        x[num] = 0


def switch_condition(x: list[list[int]], s:list[int]) -> None:
    #   s[i][0]: 성별, #s[i][1]: 자연수
    for i in range(len(x)):
        number = x[i][1]

        if x[i][0] == 1: # 남자이면
            for j in range(number-1, len(s), number):
                change(s, j)

        else: # 여자이면
            change(s, number-1) # 자연수-1(=인덱스)에 해당하는 스위치 바꾸기
            for j in range(1, len(s)//2): # 최대 (전체 길이)//2 번 가능
                if (number-1 - j) < 0 or (number-1 + j) >= len(s):
                    break   # 인덱스 범위를 벗어나면 종료

                elif s[number-1 - j] == s[number-1 + j]: # 좌우가 같으면
                    change(s, number-1 - j)
                    change(s, number-1 + j)

                else: # 좌우가 같지 않으면
                    break

    for i in range(len(s)):
        print(s[i], end = ' ')
        if i>0 and i%19 == 0:
            print()

if __name__ == "__main__":
    num = int(input())
    switch = list(map(int, input().split()))
    number_of_people = int(input())
    people = []
    for i in range(number_of_people):
        people.append(list(map(int, input().split())))

    switch_condition(people, switch)
