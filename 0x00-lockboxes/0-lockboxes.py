#!/usr/bin/python3

"""You have n number of locked boxes
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
INFO:
* Prototype: def canUnlockAll(boxes)
* boxes is a list of lists
* A key with the same number as a box opens that box
* You can assume all keys will be positive integers
* There can be keys that do not have boxes
* The first box boxes[0] is unlocked
"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened.
    Return True if all boxes can be opened, else return False
    """
    keyList = [0]

    for key in keyList:
        for box in boxes[key]:
            if (box not in keyList) and (box < len(boxes)):
                keyList.append(box)
    
    if len(keyList) == len(boxes):
        return True
    return False
