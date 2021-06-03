# Author: Timothy Jan
# Date: 05/31/2021
# Description: Determines, given a string and integer k, whether the string is a k-palindrome.


import copy


def checkPalindrome_1(string, k):
    """Given a string and integer k, returns True if the string is a k-palindrome."""
    # mathematical definition of palindrome, a single letter is a palindrome
    if len(string) == 1:
        return True

    # check if default string is a palindrome
    if pal_helper(string):
        return True

    # break up string, create permutations based on k
    original = [char for char in string]
    # pass in original
    permutations = pal_permutations([], original)
    # pass in again based on k
    if k > 1:
        for i in range(1, k):
            new_pass = copy.deepcopy(permutations)
            for string in new_pass:
                temp = pal_permutations([], string)
                for s in temp:
                    if s not in permutations:
                        permutations.append(s)

    # check if we have a k-palindrome
    for string in permutations:
        if pal_helper(string):
            return True
    return False


def pal_helper(string):
    i = 0
    j = len(string) - 1
    while i != j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True


def pal_permutations(permutations, string):
    """Takes a string and returns a list of substrings with one of each character removed from the passed string."""
    for i in range(len(string)):
        temp = []
        for j in range(len(string)):
            if i != j:
                temp.append(string[j])
        permutations.append(temp)
    return permutations


def checkPalindrome_2(string, k):
    # mathematical definition of palindrome, a single letter is a palindrome
    if len(string) == 1:
        return True

    # check if default string is a palindrome
    if pal_helper(string):
        return True

    # otherwise, call pal_helper_2 to check taking k into account
    return pal_helper_2(string, k)


def pal_helper_2(string, k):
    i = 0
    j = len(string) - 1
    count = 0
    while i < j:
        if string[i] != string[j] and count < k:
            count += 1
        if count >= k:
            return False
        i += 1
        j -= 1
    return True


w = "four"
# print(checkPalindrome_1(w, 2))
print(checkPalindrome_2(w, 3))

w = "racecar"
# print(checkPalindrome_1(w, 1))
print(checkPalindrome_2(w, 2))

w = "abcdcba"
# print(checkPalindrome_1(w, 1))
print(checkPalindrome_2(w, 0))

w = "abcdeba"
# print(checkPalindrome_1(w, 2))
print(checkPalindrome_2(w, 1))
