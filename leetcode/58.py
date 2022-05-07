s = "Hello World"
s= ''

try:
    s = s.split()
    print(len(s[-1]))
except Exception:
    print(0)