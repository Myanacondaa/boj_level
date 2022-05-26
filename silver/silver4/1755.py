m, n = map(int, input().split())
dic = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
       '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}

res = {}
for i in range(m, n+1):
    tmp = str(i)
    if i <= 9:      # 정수가 한 자리 자연수라면
       res[i] = dic[tmp]

    else:           # 정수가 두 자리 자연수라면
        res[i] = dic[tmp[0]] + ' '+ dic[tmp[1]]

res = sorted(res, key=lambda x: res[x])

for i in range(len(res)):
    if i > 0 and i % 10 == 0:       # 한 줄에 열개씩 출력
        print()

    print(res[i], end=' ')
