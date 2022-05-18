ss = ['a', 'b', 'c']
ii = [1, 2, 3]

si = [('a', 1), ('b', 2), ('c', 3)]

for _ in zip(*si):  # 加*解zip
    print(_)
