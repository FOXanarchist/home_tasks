A = [['abc', 123],['dfg']]
U = {}
for i in A:
    try:
        U[i[0]] = i[1]
    except IndexError:
        U[i[0]] = None
