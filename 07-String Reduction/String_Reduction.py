def stringReduction(s):
    # Define the set of possible characters
    given_set = {'a', 'b', 'c'}

    # Initialize the index
    i = 0

    # Iterate through the string
    while i < len(s) - 1:
        # If two adjacent characters are different
        if s[i] != s[i + 1]:
            # Find the character to replace them with
            insert_elm = given_set - {s[i], s[i + 1]}
            replacement = insert_elm.pop()
            # Replace the two different characters with the new character
            s = s[:i] + replacement + s[i + 2:]
            # Move the index back if not at the start
            i = i if i == 0 else i - 1
        else:
            # Move to the next character
            i += 1

    # Return the length of the reduced string
    return len(s)

if __name__ == '__main__':
    print(stringReduction("aacbbabcabacbccbacaac"))
    print(stringReduction("cab"))
    print(stringReduction("ccccc"))
