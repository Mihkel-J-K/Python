päev = int(input(""))
counter = 0
for i in range(1, päev + 1):
    print(i*(päev-counter))
    counter += 1
