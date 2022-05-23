dictionary = {}
for t in range(0, int(input())):
    i = input()
    try:
        dictionary[i] += 1
    except:
        dictionary[i] = 1
occurance = ""
for x in dictionary.keys():
    occurance += f"{dictionary[x]} "
print(f"{len(dictionary.keys())}\n{occurance[0:-1]}")