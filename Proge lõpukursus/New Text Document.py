def longest_unique_substring(text: str) -> str:
    substring = [""]
    counter = 0
    for x in range(0,len(text)):
        for i in text[x:]:
            print(text[x:])
            if i.lower() not in substring[counter].lower():
                substring[counter] += f"{i}"
            else:
                counter += 1
                substring += [i]
        substring += [""]
        counter += 1
    print(sorted(substring, key= len, reverse= True))

    return(sorted(substring, key= len, reverse= True)[0])

print(longest_unique_substring('nybuigmcwutymloedafpzinwbohnmrynxdkvwdsx'))