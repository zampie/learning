import numpy

lis = list(range(0, 1000001))
numpy.random.shuffle(lis)

avg = sum(lis) / len(lis)
print(avg)

momentum = 0.01
run_avg = 0
win_len = 10

for i in range(len(lis) - win_len + 1):
    # print(i, ':', i+win_len)
    # print(len(lis[i: i + win_len]))
    run_avg = (1 - momentum) * run_avg + momentum * (sum(lis[i: i + win_len]) / win_len)

print(run_avg)