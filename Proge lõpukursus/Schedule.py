import re

def create_schedule_file(input_filename: str, output_filename: str) -> None:
    output = open(output_filename, 'w')
    output.write(create_schedule_string(open(input_filename, 'r').read()))
    output.close()


def normalize(hours, minutes):
    if len(minutes) == 1:
        minutes = "0"+minutes
    if int(hours) == 0:
        return(f"12:{minutes} AM")
    elif int(hours) <= 11:
        return(f"{int(hours)%12}:{minutes} AM")
    elif int(hours) == 12:
        return (f"12:{minutes} PM")
    else:
        return(f"{int(hours)%12}:{minutes} PM")


def create_schedule_string(input_string: str) -> str:
    raamatukogu = {}
    pattern = r"( [0-9]{1,2})[^0-9]([0-9]{1,2})( {1,})([a-zA-Z]{1,})"
    sort1 = sorted(re.finditer(pattern, input_string), key = lambda f: (int(f.group(2))))
    for i in sorted(sort1, key = lambda f: (int(f.group(1)))):
        #group(1) tunnid, group(2) minutid, group(4) sõna, group(0) kõik
        if((int(i.group(1)) >= 0) and (int(i.group(1)) <= 23) and (int(i.group(2)) >= 0) and (int(i.group(2)) <= 59)):
            try:
                if(i.group(4).lower() not in raamatukogu[f'{normalize(i.group(1), i.group(2))}']):
                    raamatukogu[f'{normalize(i.group(1),i.group(2))}'].append(i.group(4).lower())
            except:
                raamatukogu[f'{normalize(i.group(1),i.group(2))}'] = [i.group(4).lower()]
    for i in raamatukogu:
        raamatukogu[i] = ", ".join(raamatukogu[i])
    if raamatukogu != {}:
        nimekiri = ''
        lenght_items = max([len(raamatukogu[i]) for i in raamatukogu] + [len("items")])
        lenght_times = max([[len(max(raamatukogu.keys(), key=len))], [len("time")]])[0]
        nimekiri += f"{'-'*(lenght_times + lenght_items + 7)}\n"
        nimekiri += f"| {' '*(lenght_times-len('time'))}time | items {' '*(lenght_items-len('items'))}|\n"
        nimekiri += f"{'-' * (lenght_times + lenght_items + 7)}\n"
        for i in raamatukogu.keys():
            nimekiri += f"| {' '*(lenght_times-len(i))}{i} | {raamatukogu[i]} {' '*(lenght_items-len(raamatukogu[i]))}|\n"
        nimekiri += f"{'-' * (lenght_times + lenght_items + 7)}\n"
        return(nimekiri)
    else:
        return("------------------\n|  time | items  |\n------------------\n| No items found |\n------------------")


create_schedule_file("s6neraamatukogu.txt", "scheduleraamat.txt")