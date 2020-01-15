def isnumber(s):
    states=[{},
            # State (1) - initial state (scan ahead thru blanks)
            {'blank': 1, 'sign': 2, 'digit':3, '.':4},
            # State (2) - found sign (expect digit/dot)
            {'digit':3, '.':4},
            # State (3) - digit consumer (loop until non-digit)
            {'digit':3, '.':5, 'e':6, 'blank':9},
            # State (4) - found dot (only a digit is valid)
            {'digit':5},
            # State (5) - after dot (expect digits, e, or end of valid input)
            {'digit':5, 'e':6, 'blank':9},
            # State (6) - found 'e' (only a sign or digit valid)
            {'sign':7, 'digit':8},
            # State (7) - sign after 'e' (only digit)
            {'digit':8},
            # State (8) - digit after 'e' (expect digits or end of valid input) 
            {'digit':8, 'blank':9},
            # State (9) - Terminal state (fail if non-blank found)
            {'blank':9}]
    current_state = 1 #start with 1st state
    for char in s:
        if char in "0123456789":
            char = "digit"
        elif char in " \t\n":
            char = "blank"
        elif char in "-+":
            char = "sign"
        if char not in states[current_state]:
            return False
        current_state = states[current_state][char]
    if current_state not in {3,5,8,9}:
        return False
    return True
    
    

print(isnumber(s=" -99e2 "))