"""Recursion vs loops."""


def loop_reverse(s: str) -> str:
    return (s[-1::-1])

def recursive_reverse(s: str) -> str:
    if len(s) > 1:
        return(recursive_reverse(s[1:]) + s[0])
    else:
        return(s)

def loop_sum(n: int) -> int:
    return(sum([i for i in range(0,n+1)]))


def recursive_sum(n: int) -> int:
    if n > 0:
        return(recursive_sum(n-1) + n)
    return(0)

print(recursive_reverse(recursive_reverse("kooj")))
print(recursive_sum(8))