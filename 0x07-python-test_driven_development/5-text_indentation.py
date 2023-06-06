#!/usr/bin/python3

""" Defines a function to print text with 2
    -new lines after a '.' , ':' and '?'
"""


def text_indentation(text):
    """ print text with 2 new lines after a
      '.' , ':' and '?'
      args:
            text(str): text to be printed
      raise:
            TyypeError: if text is not a str
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for letter in ".?:":
        if letter == ":" or letter == "?" or letter == ".":
            text = text.replace(letter, letter + "\n\n")
    new_text = [lines.strip(' ') for lines in text.split('\n')]
    final_text = "\n".join(new_text)
    print(final_text, end="")
