#!/usr/bin/python3
def no_c(my_string):
    translator = {ord(letter): None for letter in 'cC'}
    new_string = my_string.translate(translator)
    return new_string
