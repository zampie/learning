
def pkg1(cost, value, max_cost):





if __name__ == '__main__':
    cost = [1, 3, 4]
    value = [15, 20, 30]
    max_cost = 4
    # [[0, 0, 0, 0, 0], [0, 15, 15, 15, 15], [0, 15, 15, 20, 35], [0, 15, 15, 20, 35]]

    res = pkg1(cost, value, max_cost)
    print("res: ", res)