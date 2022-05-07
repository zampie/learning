it = iter([3, 4, 5, 6])
type(it)

gen = (x ** 2 for x in [1, 2, 3, 4, 5])
type(gen)

lis = [x ** 2 for x in [1, 2, 3, 4, 5]]
type(lis)

for i, v in enumerate([1, 2, 3, 4, 5], 3):
    print(i, v)

questions = ['name', 'age']
answers = ['cheng', '17']

answers = ['cheng', '17', '?']

for q, a in questions, answers:
    print(q, a)

for q, a in zip(questions, answers):
    print(q, a)

type(zip(questions, answers))

distance = lambda a, b: (a ** 2 + b ** 2) ** 0.5
distance(3, 4)

a=3
b=4
l1 = [1,2,4]
l2= [4,52]

def swap1(a,b):
    a,b = b,a

swap2 = lambda a,b: b

res = swap2(a,b)


def ap():
    l2 = [3,45]
    l1.append(l2)
    l2.append(99)
    l1.append(l2)

l1 = [1]
ap()

print(l1)


l1 = [1]

l2 = [3, 45]
l1.append(l2)
l2.append(99)
l1.append(l2)
print(l1)
