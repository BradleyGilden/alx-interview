#!/usr/bin/python3

"""
This module contians the solution to the lockbox challenge

Author: Bradley Dillion Gilden
Date: 08-01-2024
"""


def canUnlockAll(boxes):
    """returns true if all boxes can be unlocked, false otherwise"""
    # keeps track of current keys
    keys = set()
    # keep track of deleted keys
    deleted = set()
    kval = 0
    # initialize key set with first box contents or a key without a box
    keys.update(boxes[0]) if type(boxes[0]) is list else keys.add(boxes[0])
    # get the number of locked boxes excluding first box that was opened
    lboxes = len([i for i, item in enumerate(boxes)
                  if type(item) is list and i != 0])
    # break the while loop if all boxes were opeend or all the keys are used
    while (lboxes > 0 and keys.difference(deleted)):
        # use any arbitrary key to get the new keys that have not been used
        kval = keys.difference(deleted).pop()
        # update key index with new keys
        (keys.update(boxes[kval])
         if type(boxes[kval]) is list else keys.add(boxes[kval]))
        # add used keys to deleted keys set
        deleted.add(kval)
        # cross off locked boxes that were opened
        lboxes -= 1

    if (lboxes):
        return False
    else:
        return True


if __name__ == '__main__':
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
