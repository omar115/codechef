for _ in range(int(input())):
    number1,number2 = input().split()
    a = int(number1)
    b = int(number2)
    if a == b:
        print('=')
    else:
        print('<' if a < b else '>')
