#!/usr/bin/python3

"""
Module that determines if n boxes can be opened in number of locked boxes.
"""


def canUnlockAll(boxes):
    """
    Checks if boxes can be opend or not
    """
    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for x in range(1, len(boxes) - 1):
        """
        checks for checked boxes
        """

        checked = False
        for idx in range(len(boxes)):
            checked = x in boxes[idx] and x != idx
            if checked:
                break
        if checked is False:
            return checked
    return True
