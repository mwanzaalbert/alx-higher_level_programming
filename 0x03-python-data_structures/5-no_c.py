#!/usr/bin/python3
def no_c(my_string):
    translator = str.maketrans("", "", 'cC')
    new_string = my_string.translate(translator)
    return new_string
