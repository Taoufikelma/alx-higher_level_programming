#!/usr/bin/python3
"""file append module"""


def append_write(filename="", text=""):
    """append to file
        Args:
            filename: the file name
            text: the text to append
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
