N = int(input())
meeting = []
for _ in range(N):
    meeting.append(list(map(int, input().split())))

meeting.sort(key=lambda x: (x[1], x[0]))

count = 1
min_time = meeting[0][1]

for i in range(1, len(meeting)):
    if min_time <= meeting[i][0]:
        count += 1
        min_time = meeting[i][1]

print(count)