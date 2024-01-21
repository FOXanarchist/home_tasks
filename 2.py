def first():
    s = input('Input your string: ')
    A = []
    c = 0
    m = 0
    for i in s:
        if (i in A )== False:
            A.append(i)
            c+=1
            if m < c: m =c
        else:
            c = 0
            A = []

    print(m)

def second():
    s = input()
    s = s.lower()
    A = list(map(str, s.split(' ')))
    A.reverse()
    s = ''
    for i in A:
        s+=i+' '
    s =s[0].upper()+ s[1:-1]
    print(s)

def third():
    s = input()
    a = ''

    A = []
    U ={
        ')':'(',
        '}':'{',
        ']':'['
    }
    m = 0
    c = 0
    f=-1
    for i in s:
        if i in '({[':
            a += i
            c+=1
            if m < c: m = c
        elif i in ')}]' and a != '' and U[i] == a[-1]:
            a = a[:-1]
            c+=1
            if m < c: m = c
        else:
            f +=1
            A.append(a)
            a = ''
            c = 0
    if f == -1:
        print(True)
    else:print(A[f])
def main():
    third()

if __name__ == "__main__":
    main()