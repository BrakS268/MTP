def MulitiplicationTable(n, m):
    for i in range(n, m + 1):
        for j in range(n, m + 1):
            print(f"{i * j:3}", end=" ")
        print()


MulitiplicationTable(1, 35)
