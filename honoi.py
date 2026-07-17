def hanoi(n,torre1 ="A",torre2="B",torre3="C"):

    if n == 1:
        print(f"O disco 1 saiu da {torre1} e moveu para a {torre3}")
        return
    hanoi(n -1,torre1,torre3,torre2)

    print(f"O disco {n} saiu da {torre1} e moveu para a {torre3}")
    hanoi(n -1,torre2,torre1,torre3)

