ReverseTheNamesToCorrectOrders

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
