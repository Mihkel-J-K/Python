"""Order names by popularity."""

from collections import Counter

def read_from_file() -> list:
    """
    Create the list of all the names.

    :return: list
    """
    names = []
    with open("popular_names.txt", encoding='utf-8') as file:
        for line in file:
            names.append(line.strip())
    return names

    
def to_dictionary(names: list) -> dict:
    """
    Make a dictionary from a list of names.

    :param names: list of all the names
    :return: dictionary {"name:sex": number}
    """
    return Counter(names)


def to_sex_dicts(names_dict: dict) -> tuple:
    F_dict = {}
    M_dict = {}
    for i in names_dict:
        if i[-1] == "F":
            F_dict[i[0:-2]] = names_dict[i]
        else:
            M_dict[i[0:-2]] = names_dict[i]
    return M_dict, F_dict
    
    """
    Divide the names by sex to 2 different dictionaries.

    :param names_dict: dictionary of names
    :return: two dictionaries {"name": number}, {"name": number}
    first one is male names, seconds is female names.
    """
    pass


def most_popular(names_dict: dict) -> str:
    if len(names_dict) == 0:
        return "Empty dictionary."
    return Counter(names_dict).most_common(1)[0][0][0:-2]
    """
    Find the most popular name in the dictionary.

    If the dictionary is empty, return "Empty dictionary."
    :param names_dict: dictionary of names (key is name, value is count)
    :return: string
    """
    pass


def number_of_people(names_dict: dict) -> int:
    return sum(Counter(names_dict).values())
    """
    Calculate the number of people in the dictionary.

    :param names_dict: dictionary of names (key is name, value is count)
    :return: int
    """
    pass


def names_by_popularity(names_dict: dict) -> str:
    string = ""
    counter = 1
    for i in sorted(names_dict.items(), key = lambda nd: (nd[1]), reverse = True):
        string += f"{counter}. {i[0][0:-2]}: {i[1]}\n"
        counter += 1
    return string
    r"""
    Create a string used to print the names by popularity.

    Format:
        1. name: number of people + "\n"
        ...

    Example:
        1. Kati: 100
        2. Mati: 90
        3. Nati: 80
        ...

    :param names_dict: dictionary of the names (key is name, value is count)
    :return: string
    """
    pass
'''
print(to_dictionary(read_from_file()))
print(to_sex_dicts(to_dictionary(read_from_file())))
print(most_popular(to_dictionary(read_from_file())))
print(number_of_people(to_dictionary(read_from_file())))
'''
print(names_by_popularity(to_dictionary(read_from_file())))
