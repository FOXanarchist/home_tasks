def req(temp, S):
    # Расстановка знаков "+" и "-"
    if temp.count(" ") > 0:
        plus = req(temp.replace(" ", "+", 1), S)
        if plus:
            return plus
        minus = req(temp.replace(" ", "-", 1), S)
        if minus:
            return minus
        return None
    
    operator = ""
    num = 0
    c_num = ""

    for i in temp:
        if i in {"+", "-"}:
            operator = i
        else:
            c_num += i
            continue

        newNum = int(c_num)
        if operator == "+":
            num += newNum
        elif operator == "-":
            num -= newNum
        c_num = ""

    if c_num:
        newNum = int(c_num)
        if operator == "+":
            num += newNum
        elif operator == "-":
            num -= newNum

    # сравнивание результата с ответом
    if num == S:
        return f"{temp} = {S}"

    return None


def main():
    with open("lab1.txt") as file:
        temp = file.readline()
        A = list(map(int, temp.split()))
        s = A.pop()
        # Получение строки начиная с индекса 1-го пробела и заканчивая индексом последнего
        temp = temp[temp.find(" ")+1:temp.rfind(" ")]
        
        answer = req(temp, s)
        # Запись результата 
        if answer:
            print(answer)
            with open("outpute.txt", "w") as file:
                file.write(answer)
        else:
            print("no solution")
            with open("outpute.txt.txt", "w") as file:
                file.write("no solution")

if __name__ == "main":
    main()