from collections import Counter
count = int(input(""))
list_o_stuff = {}
list_o_santa = []
for i in range(0,count):
    u = input("")
    list_o_stuff[u] = int(input(""))
count2 = int(input(""))
for i in range(0,count2):
    list_o_santa += [input("")]
counted = Counter(list_o_santa)
for i in list_o_stuff:
    if i not in list_o_santa:
        counted[i] = 0
most_prized = counted.most_common(1)[0][0]
least_prized = counted.most_common()[:-2:-1][0][0]
biggest_cost = list_o_stuff[most_prized]
smallest_cost = min(list_o_stuff, key = lambda i:list_o_stuff[i])
list_o_stuff[most_prized] = list_o_stuff[smallest_cost]
list_o_stuff[smallest_cost] = biggest_cost
for i in counted:
    counted[i] = counted[i]*list_o_stuff[i]
print(sum(counted.values()))
