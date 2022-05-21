n = int(input())
card = []
for i in range(n):
    tmp = list(map(int, input().split()))       # 한 사람이 가지고 있는 5개의 카드 숫자
    sum_card = sum(tmp)                     # 다섯개의 카드의 합
    three_card_sum = []                     # 세 숫자의 합을 담을 리스트
    for j in range(len(tmp)-1):
        for k in range(j+1, len(tmp)):
            # 다섯개의 카드의 합에서 두 개의 카드 숫자를 뺌 = 세 카드의 숫자의 합
            # 그 결과를 문자열로 전환 후 문자열 뒤집기
            #  > 일의 자리가 가장 큰 수가 전체 문자열 중 가장 큰 수가 됨
            three_card_sum.append(str(sum_card - tmp[j] - tmp[k])[::-1])
    card.append(max(three_card_sum)[0])        # 일의 자리가 가장 큰 수 저장

# card 리스트 중 가장 큰 일의 자리를 가진 사람이 여러명일 경우 가장 큰 인덱스를 출력해야하므로
# 중복값을 가진 사람 인덱스 담는 result 리스트
result = list(filter(lambda x: card[x] == max(card), range(len(card))))

print(max(result)+1)


