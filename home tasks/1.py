def ch(b):
        k = 0

        while b > 0:
            b = b // 10
            k += 1
        return k
def first():
    n = int(input())
    pol = 0
    a = n
    b = n

    while a > 0:
        x = a % 10
        pol += 10 ** (ch(a) - 1) * x
        a = (a // 10)
        print(pol, a)

    if pol == a:
        print(True)
    else:
        print(False)

def second():
    a = int(input())
    pol = 0
    n_a = a
    pr = a

    if a >= 0:
        while n_a > 0:
            n = n_a % 10
            pol += 10 ** (ch(n_a) - 1) * n
            n_a = (n_a // 10)

    else:
        pr = a * (-1)
        n_a = a * (-1)
        while n_a > 0:
            n = n_a % 10
            pol += 10 ** (ch(n_a) - 1) * n
            n_a = (n_a // 10)
        pol = pol * (-1)

    if -128 <= pol <= 128:
        print(pol)

    else:
        print('no solution')

def third():
    s = input()
    A1 = ''
    A2 = ''
    A3 = ''

    i = 1
    while s != '':
        if i == 1:
            A1+=s[0]
        elif i == 2:
            A2+=s[0]
        elif i == 3:
            A3+=s[0]
        elif i == 4:
            A2+=s[0]
            i = 0
        i+=1
        s = s[1:]
    print(A1+A2+A3)
    
def main():
    first()
    second()
    third()
if __name__ == "__main__":
    main()