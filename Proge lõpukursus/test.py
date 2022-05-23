s = "py-th-on"
s.replace("-", "", 1)
print(s)

def a(x, y):
    print("a")

def b(x):
    print("b")

b(a(b(2), b(1)))

a = "karusmarjakauss"
print(a[2:-1:3])

def f(second=1, first=2):
    pass

word, solution = "hei", ""
for x in range(3):
        solution += word[-1 * x:]
print(solution)

d = {1: 2, 4: 2}
d[d[4]] = d[4]
print(d.values())

a = True
c = 5
b = c > 5

print(not a or b and a, 3 < c < 2 or not b == a)

word, solution = "adus", ""
for x in range(3):
        solution += word[:2 * x + 1]
print(solution)

def hello(a):
    print("h")
    return 3 * a

def world(b, a):
    print("w")
    a += b
    return a - b
world(hello(1), world(2, 1))

a = "Lumememm"
print(a[2::2])

a = [2, 1, 2, 3, 4]
a.remove(2)
print(a)

a = 7
b = a ** (a % 5)
a = b + b // a
print(a)


try:
    print(int(x))
except NameError:
    print("2")
except:
    print("3")

word, solution = "adus", ""
for x in range(3):
    solution += word[:2 * x + 1]
print(solution)

def k(data: int):
    return data * 2 +1
print(k(1))

for i in range (1,3):
    print(i)