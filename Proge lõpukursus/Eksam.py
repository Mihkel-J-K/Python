def invert_repetitions(s: str) -> str:
    s_list = [x for x in s]
    counter = 0
    remember = {}
    inserter = []
    looper = 0
    for i in s_list:
        counter += 1
        try:
            if i == s_list[counter]:
                counter2 = counter
                for x in s_list[counter:]:
                    if x == i:
                        print(counter)
                        s_list.pop(counter)
                    else:
                        break
            else:
                if i in remember.keys():
                    remember[i] += 1
                else:
                    remember[i] = 1
                for y in range(remember[i]):
                    inserter += [[counter, i]]
        except:
            if i in remember.keys():
                remember[i] += 1
            else:
                remember[i] = 1
            for y in range(remember[i]):
                inserter += [[counter, i]]
    print(inserter)
    for x in inserter:
        s_list.insert((x[0]+looper), x[1])
        looper += 1
    return("".join(s_list))

"""
    Remove repeated characters and repeat single characters.

    Easier option: repeat single characters twice.
    Harder option: add 1 additional character each time you need to repeat the same char.

    Result of empty string is also empty string.

    Examples:
    'a' -> 'aa'
    'aa' -> 'a'
    'bc' -> 'bbcc'
    'bcc' -> 'bbc'
    'bbc' -> 'bcc'
    'bbcbcc' -> 'bccbbc'
    'kloo' -> 'kkllo'
    'ababbab' -> 'aabbaabaabb' (easier) or 'aabbaaabaaaabbb' (harder)
    """
print(invert_repetitions("1__1__1__1__2"))