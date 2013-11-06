def cap_first(s):
    """
    Uppercases the first letter of the string but leaves the rest unchanged
    (unlike Python's capitalize(), which uppdercase the first character and
    lowercases everything else
    """
    return s[0].upper() + s[1:]
