5-text_indentation.py
#!/usr/bin/python3
"""Defining a text-indentation function."""


def text_indentation(text):
    """
    Print text with two new lines after each '.', '?', and ':
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
