s = input()
res = 0
tmp = 1
st = []
for i in range(len(s)):
    if s[i] == '(':
        st.append(s[i])
        tmp *= 2

    elif s[i] == '[':
        st.append(s[i])
        tmp *= 3

    elif s[i] == ')':
        if not st or st[-1] == '[':     # 스택이 비어있거나 마지막이 '['일 경우
            res = 0
            break

        if st[i-1] == '(':
            res += tmp
        st.pop()
        tmp //= 2

    else:
        if not st or st[-1] == '(':  # 스택이 비어있거나 마지막이 '('일 경우
            res = 0
            break

        if st[i - 1] == ']':
            res += tmp
        st.pop()
        tmp //= 3


if st:
    print(0)

else:
    print(res)
