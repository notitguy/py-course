def add_one(num):
    if (num >= 9):
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)


add_one(0)

print('')


def add_one_loop(bum):
    while bum < 9:
        bum += 1
        print(bum)


add_one_loop(0)

# https://youtu.be/H2EJuAcrZYU?t=12224
