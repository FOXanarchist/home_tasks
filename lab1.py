def req(temp, S):
    # Замена пробелов на знаки
    c = temp.count(' ')
    if c > 0:
        req(temp.replace(' ', '+', 1),S)
        req(temp.replace(' ', '-', 1),S)
        return
    
    # Очень сложный способ посчитать строку, если пробелов не обнаружено
    answer = eval(temp) 
    if answer == S:
        f = open('outpute.txt', 'w')
        f.write(f'{temp}={S}')
        f.close()
        exit()
    

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
        req(temp, S)


if __name__ == '__main__':
    main()