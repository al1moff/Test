s = input("misol: ")
for i in range(len(s)):
    if s[i] == '+':
        print(int(s[0]) + int(s[-1]))
    elif s[i] == '-':
        print(int(s[0]) - int(s[-1]))
    elif s[i] == '*':
        print(int(s[0]) * int(s[-1]))
    elif s[i] == '/':
        print(int(s[0]) / int(s[-1]))
