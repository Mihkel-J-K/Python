kook = [1,2,3,4,5,6]
def memory_pointer(nums: list) -> str:
    if nums[0] <= len(nums):
        return(f"First element points to: {nums[0]}")
    else:
        return (f"First element points to: {nums[-1]}")

def close_far(a: int, b: int, c: int) -> bool:
    if (abs(a - b) <= 1 and abs(a - c) >= 2 and abs(b - c) >= 2) or (abs(a - c) <= 1 and abs(a - b) >= 2 and abs(b - c) >= 2):
        return(True)
    else:
        return(False)

def get_names_from_results(results_string: str, min_result: int) -> list:
    results_list = results_string.split(",")
    names = []
    for i in results_list:
        try:
            if (int(i.split(" ")[-1]) >= min_result) and (len(i.split(" ")) > 1):
               names += [" ".join(i.split(" ")[0:-1])]
        except:
            pass

    return(names)

def get_max_nums(nums):
    answer = []
    for i in nums:
        if i == max(nums):
            answer += [i]
    return(answer)

def unique_dict_items(dict1: dict, dict2: dict) -> dict:
    answer = {}
    for i in dict1.keys():
        if i not in dict2.keys():
            answer[i] = dict1[i]
    for i in dict2.keys():
        if i not in dict1.keys():
            answer[i] = dict2[i]
    return(answer)

import re
def remove_symbols_recursive(input_str: str) -> str:
    return("".join(re.split(r"[?].{0,2}", input_str)))

def remove_symbols_recursive(input_str: str) -> str:
    if len(input_str) == 0:
        return("")
    if input_str[0] == "?":
        return(remove_symbols_recursive(input_str[3:]))
    else:
        return(input_str[0] + remove_symbols_recursive(input_str[1:]))


print(remove_symbols_recursive("231?2ejda?12da?21"))