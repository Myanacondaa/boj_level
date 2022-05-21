n = int(input())        # 학생 수
score = []
for _ in range(n):
    score.append(list(map(int, input().split())))

# 나라 수만큼 각 나라의 메달 수여자 수 리스트 만들기
# 국가 코드의 최대번호 = 국가 수
country_medal = [0]*max(score[i][0] for i in range(n))      # 소속 국가의 수상자 수
score.sort(reverse=True, key=lambda x: x[2])
cnt = 0

for i in range(n):
    if cnt == 3:        # 3명의 수상자가 나오면 종료
        exit(0)
    if country_medal[score[i][0]-1] < 2:        # 소속 국가 번호의 메달 수가 2개 이하이면
        print(score[i][0], score[i][1])     # 소속 국가 번호와 학생 이름 출력

        country_medal[score[i][0] - 1] += 1     # 소속 국가 수상자 수 +1
        cnt += 1
