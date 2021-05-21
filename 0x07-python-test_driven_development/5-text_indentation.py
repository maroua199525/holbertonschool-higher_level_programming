#!/usr/bin/python3
def text_indentation(text):
    """ function prints text with lines

    args:
    text: string

    return:
     prints a text with 2 new lines after each of these characters: ., ? and :
    """
    new_text = ""
    for x in text:
        if x == '.' or x == '?' or x == ':':
            new_text += "\n\n"
        else:
            new_text += x
    print(new_text)
