import time
def req(temp, S, k):
    # Замена пробелов на знаки
    c = temp.count(' ')
    if c > 0:
        req(temp.replace(' ', '+', 1),S,k)
        req(temp.replace(' ', '-', 1),S,k)
        return
    
    #посчитать строку, если пробелов не обнаружено
    st = list(temp)
    answer = 0
    f = ''
    for i in st:
        if i in ['1','2','3','4','5','6','7','8','9','0',]:
            if f == '+':
                answer+= int(i)
            elif f == '-':
                answer -= int(i)
        elif i in ['+','-']:
            f = i

    
    # answer = eval(temp) 
    if answer == S:
        print(answer)
        f = open('outpute.txt', 'w')
        f.write(f'{temp}={S}')
        f.close()
        k = 1
        time.sleep(10)
        exit()
    else:
        f = open('outpute.txt', 'w')
        f.write('None')
        f.close()
    
    return k
def main():
    
    # Получение данных из файла
    with open('lab1.txt', 'r', encoding='utf-8') as file:
        temp = file.readline()

        # Распределение данных по переменным
        A = list(map(int, temp.split()))
        N = A.pop(0)
        S = A.pop()
        temp = temp[temp.find(' ')+1:temp.rfind(' ')]
        
        # Запуск рекурсии
        tt = req(temp, S, 0)
        if tt == 0:
            f = open('outpute.txt', 'w')
            f.write('None')
            f.close()

if __name__ == '__main__':
    main()