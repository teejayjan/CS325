# Author: Timothy Jan
# Date: 04/05/2021
# CS 325: Analysis of Algorithms
# Description: Implements algorithm that checks whether two boxes, represented by a list of coordinates, overlap.
#              Includes both recursive and linear implementations.


def doBoxesOverlap(box1, box2):
    """Determines whether two boxes, represented by a list of coordinates, overlap. Returns True if they overlap or
    False if they do not overlap or if they simply share a corner or edge."""

    # convert box1's coordinates to individual variables
    box1_x1 = box1[0]
    box1_y1 = box1[1]
    box1_x2 = box1[2]
    box1_y2 = box1[3]

    # convert box2's coordinates to individual variables
    box2_x1 = box2[0]
    box2_y1 = box2[1]
    box2_x2 = box2[2]
    box2_y2 = box2[3]

    # check box1's x-coordinates
    if box2_x1 < box1_x1 < box2_x2 or box2_x1 < box1_x2 < box2_x2:
        return True

    # check box1's y-coordinates
    if box2_y1 < box1_y1 < box2_y2 or box2_y1 < box1_y2 < box2_y2:
        return True

    # check box2's x-coordinates
    if box1_x1 < box2_x1 < box1_x2 or box1_x1 < box2_x2 < box1_x2:
        return True

    # check box2's y-coordinates
    if box1_y1 < box2_y1 < box1_y2 or box1_y1 < box2_y2 < box1_y2:
        return True
    return False


def recDoBoxesOverlap(box1, box2):
    """Recursive implementation of doBoxesOverlap."""
    return _boxes_overlap(box1, box2, 0)


def _boxes_overlap(box1, box2, index):
    # base case, we're done checking and they don't overlap
    if index > 3:
        return False

    # check x
    if index % 2 == 0:
        if box1[0] < box2[index] < box1[2] or box2[0] < box1[index] < box2[2]:
            return True
        else:
            return _boxes_overlap(box1, box2, index + 1)

    # check y
    if index % 2 != 0:
        if box1[1] < box2[index] < box1[3] or box2[1] < box1[index] < box2[3]:
            return True
        else:
            return _boxes_overlap(box1, box2, index + 1)


# unit tests
def main():
    # # examples from PDF
    # box1 = [0, 0, 2, 2]
    # box2 = [1, 1, 3, 3]
    # print("PDF 1:", doBoxesOverlap(box1, box2))  # true
    #
    # box1 = [0, 0, 1, 1]
    # box2 = [1, 0, 2, 1]
    # print("PDF 2:", doBoxesOverlap(box1, box2))  # false
    #
    # # custom tests
    # # boxes far apart
    # box1 = [0, 0, 2, 2]
    # box2 = [10, 10, 20, 20]
    # print("Boxes far apart:", doBoxesOverlap(box1, box2))  # false
    #
    # # boxes share a side
    # box1 = [0, 0, 2, 2]
    # box2 = [2, 0, 4, 2]
    # print("Share a side:", doBoxesOverlap(box1, box2))  # false
    #
    # # one corner inside each other (with negative)
    # box1 = [0, 0, 2, 2]
    # box2 = [-2, -2, 1, 1]
    # print("One corner inside the other (negative):", doBoxesOverlap(box1, box2))  # true
    #
    # # box1 is inside box2
    # box1 = [2, 2, 3, 3]
    # box2 = [1, 1, 4, 4]
    # print("Box1 inside Box2:", doBoxesOverlap(box1, box2))  # true
    #
    # # box2 is inside box1
    # box1 = [1, 1, 4, 4]
    # box2 = [2, 2, 3, 3]
    # print("Box2 inside Box1:", doBoxesOverlap(box1, box2))  # true
    #
    # # box2's side cuts through box1, but does not have a corner inside box1
    # box1 = [0, 0, 2, 2]
    # box2 = [1, -2, 5, 4]
    # print("Box2's side cuts through box1:", doBoxesOverlap(box1, box2))  # true

    # Recursive
    # examples from PDF
    box1 = [0, 0, 2, 2]
    box2 = [1, 1, 3, 3]
    print("PDF 1:", recDoBoxesOverlap(box1, box2))  # true

    box1 = [0, 0, 1, 1]
    box2 = [1, 0, 2, 1]
    print("PDF 2:", recDoBoxesOverlap(box1, box2))  # false

    # custom tests
    # boxes far apart
    box1 = [0, 0, 2, 2]
    box2 = [10, 10, 20, 20]
    print("Boxes far apart:", recDoBoxesOverlap(box1, box2))  # false

    # boxes share a side
    box1 = [0, 0, 2, 2]
    box2 = [2, 0, 4, 2]
    print("Share a side:", recDoBoxesOverlap(box1, box2))  # false

    # one corner inside each other (with negative)
    box1 = [0, 0, 2, 2]
    box2 = [-2, -2, 1, 1]
    print("One corner inside the other (negative):", recDoBoxesOverlap(box1, box2))  # true

    # box1 is inside box2
    box1 = [2, 2, 3, 3]
    box2 = [1, 1, 4, 4]
    print("Box1 inside Box2:", recDoBoxesOverlap(box1, box2))  # true

    # box2 is inside box1
    box1 = [1, 1, 4, 4]
    box2 = [2, 2, 3, 3]
    print("Box2 inside Box1:", recDoBoxesOverlap(box1, box2))  # true

    # box2's side cuts through box1, but does not have a corner inside box1
    box1 = [0, 0, 2, 2]
    box2 = [1, -2, 5, 4]
    print("Box2's side cuts through box1:", recDoBoxesOverlap(box1, box2))  # true


if __name__ == "__main__":
    main()
