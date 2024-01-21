def first():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    i = 1
    A = []
    while matrix != []:
        if i == 1:
            A += matrix.pop(0)
        if i == 2:
            for j in range(len(matrix)):
                A.append(matrix[j][-1])
                matrix[j].pop(-1)
        if i == 3:
            z = matrix.pop(-1)
            z.reverse()
            A+= z
        if i == 4:
            for j in range(len(matrix), 0, -1):
                A.append(matrix[j-1][0])
                matrix[j-1].pop(0)
            i = 0
        i+=1
    print(A)

def second():
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    B = [[]]
    for i in range(len(A)):
        for j in range(len(A[i])):
            B[i].append(A[j][i])
        B[i].reverse()
        B.append([])
    del B[-1]
    print(*B, sep='\n')

def main():
    first()
    second()

if __name__ == "__main__":
    main()