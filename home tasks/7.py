def santa_users(A):
    U = {}
    for i in A:
        try:
            U[i[0]] = i[1]
        except IndexError:
            U[i[0]] = None
    return U

def rim_converter(N:str):
    
    A = 0
    A += N.count('CM') * 900
    N.replace('CM','')
    A += N.count('CD') * 400
    N.replace('CD','')
    A+= N.count('XC')*90
    N.replace('XC', '')
    A+= N.count('XL')*40
    N.replace('XL','')
    A+= N.count('IX')*9
    N.replace('IX','')
    A+= N.count('IV')*4
    N.replace('IV', '')
    A+= N.count('M')*1000
    N.replace('M','')
    A+= N.count('D')*500
    N.replace('D','')
    A+= N.count('C')*100
    N.replace('C', '')
    A+= N.count('L')*50
    N.replace('L', '')
    A+= N.count('X')*10
    N.replace('X', '')
    A+= N.count('V')*5
    N.replace('V', '')
    A+= N.count('I')
    N.replace('I', '')
    return A

def mmm(s, l, k):
    if l != '':
        d = []
        for i in range(len(s)):
            for j in range(len(l)):
                d.append([i]+l[j])


def get_pins(s):
    U = {
        '1':'24',
        '2':'135',
        '3':'26',
        '4':'157',
        '5':'2468',
        '6':'359',
        '7':'48',
        '8':'579',
        '9':'68'
    }
    n = len(s)
    A = []
    for i in range(n):
        A.append(U[s[i]])
    for i in range(n):
        ...

if __name__ == '__main__':
    # santa_users([['abc',123],['dfg']])
    # print(rim_converter('MCM'))
    get_pins('123')
    ...