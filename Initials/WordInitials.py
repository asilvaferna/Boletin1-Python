def letters(string):
    count = 0
    for letter in string:
        if " " == letter:
            count += 1

    if count == 0:
        exit()

    splittedString = string.rsplit(" ", count + 1)

    initials = str()

    for word in splittedString:
        initials += word[0].upper()

    print (initials)

string = ""

letters(string)

