#!/bin/python3

if __name__ == '__main__':
    s = input()

diction = {}

for i in s:
    try:
        diction[i] += 1
    except:
        diction[i] = 1
sort_dict = sorted(diction.keys())
in_order = sorted(sort_dict, key = lambda x: int(diction[x]), reverse = True)
print(f"{in_order[0]} {diction[in_order[0]]}\n{in_order[1]} {diction[in_order[1]]}\n{in_order[2]} {diction[in_order[2]]}")