def sum_half_evens(nums: list) -> int:
    even = []
    for x in nums:
        if x % 2 == 0:
            even += [x]
    if len(even) % 2 == 0:
        number = len(even)//2 
        return(sum(even[0:number]))
    else:
        number = len(even)//2 + 1
        return(sum(even[0:number]))
def remove_vowels(string):
    new_word = ""
    for x in string:
        if x in "aeiou":
            pass
        else:
            new_word += x
    return(new_word)

def longest_filtered_word(string_list: list) -> str:
    longest_word = ""
    for x in string_list:
        if len(x) > len(longest_word):
            longest_word = x
    return(longest_word)

def sort_list(string_list: list) -> list:
    new_string_list = []
    for sonu in string_list:
        new_word = ""
        for x in sonu:
           if x in "aeiou":
              pass
           else:
              new_word += x
        new_string_list += [new_word]
    new_string_list.sort(key=len, reverse=True)
    return(new_string_list)
    '''
    cycle = new_string_list
    longest_list = []
    for i in cycle:
        cycleingmech = []
        longest_word = ""
        for x in cycle:
            if len(x) > len(longest_word):
                cycleingmech += [longest_list]
                longest_word = x
                longest_list = [x]
            elif len(x) == len(longest_word):
                longest_list += [x]
            else:
                cycleingmech += [x]
            print(longest_word)
        cycle = cycleingmech
    print(longest_list)
    '''
def one_set_contains_another(set1: set, set2: set) -> bool:
    if set1 ^ set2:
        print("True")
    else:
        print("False")
'''
def organise_by_first_symbol(strings: list) -> dict:
    dictionary = {}
    for x in strings:
            dictionary[x[0]] += [x]
    return(dictionary)
print(organise_by_first_symbol(["hello", "word", "world", "welcome", "yes"]))
'''

def spiraal():
    while True:
        height = int(input("Height, 5 and up"))
        lenght = int(input("Lenght, 5 and up"))
        if height >= 5 and lenght >= 5:
            break
    i = 0
    while i < height:
        i += 1
        if i%2 == 1:
            print("#"*lenght)
            print("#"+" "*(lenght-2)+"#")
            i += 1
        else:
            print("# "*(lenght//2)+"#")


def normalize_user_name(name: str) -> str:
    return(name[0].upper()+name[1::].lower())

def reverse_user_name(name: str) -> str:
    Name = name[::-1]
    return(Name[0].upper()+Name[1::].lower())

def check_user_choice(choice: str) -> str:
    if choice.lower() in ["rock","paper","scissors"]:
        return(choice.lower())
    else:
        return("Sorry, you entered unknown command")

def determine_winner(name: str, user_choice: str, computer_choice: str, reverse_name: bool = False) -> str:
    player_choice = check_user_choice(user_choice)
    if reverse_name is True:
        player_name = reverse_user_name(name)
    else:
        player_name = normalize_user_name(name)
    if (player_choice == "paper" and computer_choice == "scissors") or (player_choice == "rock" and computer_choice == "paper") or (player_choice == "scissors" and computer_choice == "rock"):
        return(f"{player_name} had {player_choice} and computer had {computer_choice}, hence computer wins.")
    elif (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock"):
        return(f"{player_name} had {player_choice} and computer had {computer_choice}, hence {player_name} wins.")
    elif player_choice == computer_choice:
        return(f"{player_name} had {player_choice} and computer had {computer_choice}, hence it is a draw.")
    else:
        return("There is a problem determining the winner.")


    
def make_dough(ingredients: list) -> int:
        return(min([ingredients.count("egg")//1, ingredients.count("milk")//5,ingredients.count("flour")//4, ingredients.count("butter")//1, ingredients.count("sugar")//2])*7)

def make_a_pancake(dough: float) -> float:
    return(round(dough - 0.8,2))

def make_n_pancakes(n: int, ingredients: list) -> int:
    dough = make_dough(ingredients)
    N = 0
    while can_make_pancake(dough):
        dough = make_a_pancake(dough)
        N += 1
    return(min(n,N))

def can_make_pancake(dough: float) -> bool:
    if(dough//0.8 >= 1):
        return(True)
    else:
        return(False)
def workday_count(days):
    return(days -(days/5)*2)
print(workday_count(int(input(""))))
a = 13
print(10 < a > 12 or not (a > 12), a and not a)
#one_set_contains_another({1, 2}, {"1", "2"})
#print(sort_list(["kook","keeks","toormoos"]))
