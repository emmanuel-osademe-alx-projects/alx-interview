#!/usr/bin/python3
"""
Lockbox task
"""

def canUnlockAll(boxes):
    """
	Determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    """
    n = len(boxes)
    opened = [0]
    for i in opened:
        for j in boxes[i]:
            if j not in opened:
                if j < n:
                    opened.append(j)
    if len(opened) == n:
        return True
    return False
