tmp = []
    file = open("Salaries.csv","r")

    n = 1
    for row in file:
        print(str(n)+".",row)
        n = n + 1

    n = 1
    for row in file:
        tmp.append(row)
        n = n + 1

    n = 1
    for row in tmp:
        print(row)
        n = n + 1