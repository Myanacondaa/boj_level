import sys
input = sys.stdin.readline
############# 시간 초과 #############
t = int(input())
for _ in range(t):
    s = list(input().rstrip())
    if s == s[::-1]:
        print(0)
        continue

    else:       # 유사회문 가능성 체크
        check = False
        for i in range(len(s)):     # 한 문자씩 제거
            tmp = s[0:i]+s[i+1:]    # 제거한 문자를 기준으로 문자열 합치기
            if tmp == tmp[::-1]:
                print(1)
                check = True
                break

        if not check:
            print(2)


