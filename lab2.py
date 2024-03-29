
class ferz():
    # рассчёт всех возможных ходов по вертикали\горизонтали
    def line(N, x, y):
        possible_moves = []
        # if x > 3:
        #     a = x-3,y
        #     possible_moves.append(a)
        # if N - x - 3>= 0:
        #     a = x+3,y
        #     possible_moves.append(a)
        # if y > 3:
        #     a = x,y-3
        #     possible_moves.append(a)
        # if N - y-3 >=0:
        #     a = x,y+3
        #     possible_moves.append(a)
        # return possible_moves
    
        for i in range(1, 4):
            if x >i:
                a = x - i, y
                possible_moves.append(a)
            if x + i <=N:
                a = x + i, y
                possible_moves.append(a)
            if y >i:
                a = x, y - i
                possible_moves.append(a)
            if (y + i) <= N:
                a = x, y + i
                possible_moves.append(a)
        return possible_moves

    # рассчёт всех возможных ходов по диагонали
    def diagonal(N, x, y):
        possible_moves = []
        # if x >=3 and y >= 3:
        #     a = x -3, y -3
        #     possible_moves.append(a)
        # if N - x - 3 >= 0 and N - y - 3 >= 0:
        #     a = x + 3, y + 3
        #     possible_moves.append(a)
        # if x>=3 and N - y - 3 >=0:
        #     a = x - 3, y + 3
        #     possible_moves.append(a)
        # if N - x - 3 >=0 and y >= 3:
        #     a = x + 3, y - 3
        #     possible_moves.append(a)
        # return(possible_moves)

        for i in range(1, 4):
        
            if x - i >0 and y - i > 0:
                a = x - i, y - i
                possible_moves.append(a)
            if N - x - i >=0 and N - y - i>=0:
                a = x + i, y + i
                possible_moves.append(a)
            if x - i >0 and N - y - i>=0:
                a = x - i, y + i
                possible_moves.append(a)
            if N - x - i >=0 and y - i > 0:
                a = x + i, y - i
                possible_moves.append(a)
        return possible_moves

# получерие зоны возможных ходов одной фигуры
def all_positons(N, x, y):
    return ferz.line(N, x, y) + ferz.diagonal(N, x, y)


# получение вводных данных из файла
def take_info(name):
    with open(f'{name}.txt', 'r', encoding='utf-8') as file:
        N, L, K = map(int, file.readline().split())
        figures = []

        for _ in range(K):
            a = tuple(map(int, file.readline().split()))
            figures.append(a)
    return N,L,K,figures

def main():
    N, L, K, figures = take_info('input')
    # формирование списка зон, которые находятся под боем расстоновленых фигур
    danger_list = []
    for i in range(len(figures)):
        danger_list+=all_positons(N, figures[i][0], figures[i][1]) + [figures[i]]
    danger_list = set(danger_list)
    danger_list = list(danger_list)
    print(*danger_list,sep='\n')

    # расстановка фигур
    placed_list = []
    for l in range(L):
        f=0
        for x in range(N):
            for y in range(N):
                tutu = x,y
                if tutu not in danger_list:
                    placed_list.append(tutu)
                    danger_list +=all_positons(N, x, y) + [tutu]
                    danger_list = set(danger_list)
                    danger_list = list(danger_list)
                    f = 1
                    break
            if f == 1:
                break
    placed_list = set(placed_list)
    placed_list = list(placed_list)
    print(*placed_list, sep='\n')
                    



    
    


if __name__ == '__main__':
    main()