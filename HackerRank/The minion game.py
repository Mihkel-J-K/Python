def minion_game(string):
    consotant = "BCDFGHJKLMNPQRSTVWXYZ"
    vowel = "AEIOU"
    repeator = 0
    Kevin = 0
    Stuart = 0
    for i in string:
        if i in vowel:
            Kevin += len(string) - repeator
        if i in consotant:
            Stuart += len(string) - repeator
        repeator += 1
    if Kevin == Stuart:
        print("Draw")
    elif Kevin >= Stuart:
        print(f"Kevin {Kevin}")
    else:
        print(f"Stuart {Stuart}")

if __name__ == '__main__':
    s = input()
    minion_game(s)