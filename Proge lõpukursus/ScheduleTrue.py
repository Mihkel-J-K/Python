import re
tekst= "18:19 Donec blandit, est nec semper convallis, arcu 7.01 libero lacinia ex, eu placerat risus est non tellus."
def create_schedule_string(input_string: str) -> str:
    pattern = "/[0-9]{1,2}[^a-z^A-Z][0-9]{1,3} {1,}[a-zA-Z]{1,}/gm"
    found = re.search(pattern,input_string)
    return(found)
    """Create schedule string from the given input string."""
    pass

print(create_schedule_string(tekst))