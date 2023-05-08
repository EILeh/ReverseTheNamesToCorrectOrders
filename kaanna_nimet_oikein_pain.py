"""
Reverse the names to correct orders

The program changes a string containing such a name to the order, where the
first name is followed with the last name. The names are separated with a space
and the comma as well as all unnecessary spaces are removed. The function
returns the modified name. It is assumed that the name string contains no
more than one comma and that the caller of the function always passes at least
one character as a parameter value (an empty string "" cannot be a parameter
value). If the first of the last name has been forgotten, but the comma has been
given, only the first or the last name is returned without the
comma and unnecessary spaces. If the name does not contain a first name nor a
last name (it is just a comma), an empty string "" is returned. It is assumed
that the name is correct and the name is returned as such, if it does not
contain a comma.

Writer of the program: EILeh
"""


def reverse_name(name):
    """
    Prints the given names but in reverse and without comma
    and spaces in the front and the end.
    :param name: list, given names
    """
    # testname = [X, ]
    # testname[0] -> last name
    # testname[1] -> first name
    fullname = ""
    comma = ","
    space = ""

    # Katetut tapaukset: pelkkä pilkku, pelkkä etunimi, pelkkä sukunimi, koko
    # nimi ilman pilkkua, jomalla kummalla puolella oli nimi ja toisella pelkkää
    # välilyöntiä tai tyhjä merkkijono

    # If input is only a comma.
    if name == comma:
        return space

    # If input doesn't have a comma, all the possible spaces are removed
    # around the input and the input itself is returned.
    if comma not in name:
        stripped_name = name.strip()
        return stripped_name

    # At this point, it is certain that there is a comma in the input.
    splitted_name_list = name.split(",")

    first_name = splitted_name_list[1]
    last_name = splitted_name_list[0]

    stripped_first_name = first_name.strip()
    stripped_last_name = last_name.strip()

    # If first name is empty.
    if stripped_first_name == "":
        return stripped_last_name

    # If last name is empty.
    elif stripped_last_name == "":
        return stripped_first_name

    # If there is both first name and last name, the fullname is returned as
    # wanted.
    else:
        fullname = stripped_first_name + " " + stripped_last_name
        return fullname


def main():

    name = []

    reverse_name("")

if __name__ == "__main__":
    main()