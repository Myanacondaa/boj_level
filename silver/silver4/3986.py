n = int(input())
cnt = 0
for _ in range(n):
    s = input()  # A와 B로만 이루어진 문자열
    st = []  # 스택

    for i in range(len(s)):
        if st:          # 스택이 비어있지 않다면
            if s[i] == st[-1]:
                st.pop()
            else:
                st.append(s[i])
        else:
            st.append(s[i])

    if not st:      # 스택이 비어있지 않다면 좋은 단어를 의미
        cnt += 1

print(cnt)