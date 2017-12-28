def get_strings(num):
    """
    -------------------------------------------------------
    Takes a series of inputs from a user and displays them
    as items on a list
    -------------------------------------------------------
    Preconditions:
        num - the user chosen input for the list (str)
    Postconditions:
        returns
        values - returns the list (list)
    -------------------------------------------------------
    """
    values = []

    while num != "":
        num = input("Enter item: ")
        if num == "":
            values = values
        else:
            values.append(num)

    return values
