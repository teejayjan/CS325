# Author: Timothy Jan
# Date: 04/05/2021
# CS 325: Analysis of Algorithms
# Description: Implements algorithm that, given a list of numbers corresponding to days of the week, returns what day
#              has the majority of birthdays. Uses "Divide and Conquer" recursive technique.

# [1, 2, 3, 4,  5, 6,  7]
# [M, T, W, Th, F, Sa, Su]


def MajorityBirthdays(arr):
    """Determines, given a list of numbers representing days of the week from Monday = 1 to Sunday = 7, what day of
    the week the majority of listed birthdays falls on. ***Assumes there will be a solution (don't use with arrays
    with ties)***"""

    for i in arr:
        frequency = _num_days(arr, 0, len(arr) - 1, i)
        if frequency > len(arr) // 2:
            return i


def _num_days(arr, start, end, day):
    """Helper function to count occurrences of days in original array."""

    if start < end:
        return _num_days(arr, start, (start + end) // 2, day) + _num_days(arr, ((start + end) // 2) + 1, end, day)
    if start == end and day == arr[start]:
        return 1
    else:
        return 0


def main():
    # PDF Examples
    arr = [3, 2, 3]
    print("3:", MajorityBirthdays(arr))

    arr = [2, 2, 1, 1, 1, 2, 2]
    print("2:", MajorityBirthdays(arr))

    # other tests
    arr = [7, 7, 7, 7, 7, 1, 2, 3]
    print("7:", MajorityBirthdays(arr))

    arr = [5, 5, 5, 5, 5, 7, 1, 2]
    print("5:", MajorityBirthdays(arr))

    arr = [1, 2, 1, 2, 1, 2, 1, 2, 1]
    print("1:", MajorityBirthdays(arr))

    arr = [4]
    print("4:", MajorityBirthdays(arr))

    arr = [1, 1, 1, 2, 2]
    print("1:", MajorityBirthdays(arr))

    arr = [1, 1, 2, 2, 2]
    print("2:", MajorityBirthdays(arr))

    arr = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
    print("6:", MajorityBirthdays(arr))


if __name__ == "__main__":
    main()
