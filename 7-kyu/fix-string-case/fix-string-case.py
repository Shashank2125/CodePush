def solve(s):
    upper=0
    lower=0
    for ch in s:
        if ch.isupper():
            upper+=1
        if ch.islower():
            lower+=1
    if upper>lower:
        return s.upper()
    else:
        return s.lower()