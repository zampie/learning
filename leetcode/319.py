
for n in range(1, 50):
    status = [0] * n

    for turn in range(1, n + 1):
        for i in range(turn - 1, n, turn):
            status[i] ^= 1
        # print(status)

    print(n, " : ", sum(status))



