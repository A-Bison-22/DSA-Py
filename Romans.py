def getHindu(roman):
    roman = roman.lower()  # Convert input to lowercase for uniform processing

    # Dictionary mapping Roman numerals to their Hindu-Arabic (decimal) values
    reg = {
        "m": 1000,
        "d": 500,
        "c": 100,
        "l": 50,
        "x": 10,
        "v": 5,
        "i": 1
    }

    # Handle empty string input (can return 0 or raise an error here we return 0)
    if not roman:
        return 0
                                                                                                                        # A simple program that converts roman numerals to Hindu numerals.
                                                                                                                        # Thought about this late last night, no relevance to my usual stuff
    try:
        idx = 0
        total = 0

        # Iterate through all but the last character
        while idx < len(roman) - 1:
            # If current value is less than next, subtract it (e.g., IV = 5 - 1)
            if reg[roman[idx]] < reg[roman[idx + 1]]:
                total -= reg[roman[idx]]
            else:
                total += reg[roman[idx]]
            idx += 1

        # Add value of the last character (always added)
        total += reg[roman[-1]]
        return total

    # tell user to fuck off if the roman equivalent doesn't exist
    except KeyError:
        return -1


print(getHindu(""))  

"""

Contrary to popular belief, there was no strict rule preferring IV over IIII, there weren't many rules at all
many older clocks still use IIII instead of IV The Roman system was very disconnected and it was mostly the 
Vatican deciding the conventions for it in the medieval times So no, i will not be adding a system to verify 
IIII over IV, because i'm lazy. 

"""