s = input()
if "U" in s:
    s = s[s.index("U"):]
    if "C" in s:
        s = s[s.index("C"):]
        if "P" in s:
            s = s[s.index("P"):]
            if "C" in s:
                print("I love UCPC")
            else:
                print("I hate UCPC")
        else:
            print("I hate UCPC")
    else:
        print("I hate UCPC")
else:
    print("I hate UCPC")

