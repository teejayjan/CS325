# Author: Timothy Jan
# Date: 04/26/2021
# Description: Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest
#              of the intervals non-overlapping.


def intervals_bf(arr):
    """Finds minimum number of intervals to remove to make the rest of the intervals non-overlapping. Brute Force."""
    arr.sort()
    count = 0
    for i in range(len(arr) - 1):
        if arr[i][0] >= arr[i + 1][0] and arr[i][1] <= arr[i + 1][1]:
            count += 1
    return count


print(intervals_bf([[1, 2], [2, 3], [3, 4], [1, 3]]))
print(intervals_bf([[1, 2], [1, 2], [1, 2]]))
print(intervals_bf([[1, 2], [2, 3]]))
print()


def intervals_greedy(arr):
    """Finds the minimum number of intervals to remove to make the rest of the intervals non-overlapping. Greedy."""
    arr.sort()
    og_len = len(arr)
    temp = [arr[0]]
    for i in range(1, og_len):
        if arr[i] > temp[-1]:
            temp.append(arr[i])
    return og_len - len(temp)



print(intervals_greedy([[3, 4], [1, 2], [2, 3], [3, 4], [1, 3]]))
print(intervals_greedy([[1, 2], [1, 2], [1, 2]]))
print(intervals_greedy([[1, 2], [2, 3]]))
print(intervals_greedy([[1, 8], [2, 3], [3, 4], [5, 6], [6, 7], [4, 8]]))
