# Author: Timothy Jan
# Date: 05/31/2021
# Description: Determines, given a string and a pattern of characters and symbols, whether the string and pattern match.


def patternmatch(string, p):
    """Determines, given a string and a pattern of characters and symbols, whether the string and pattern match."""

    # pattern is a singular "*", we can exit early
    if p == "*":
        return True

    m = len(string)
    n = len(p)

    dp = [[False for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            # Base case: "" == "" (row and column zero are empty strings)
            if i == 0 and j == 0:
                dp[i][j] = True

            # Row 0: can be true if first * or uninterrupted string of * ("*" can equal empty string)
            if i == 0 and p[j - 1] == "*":
                # pattern starts with an "*"
                if j == 1:
                    dp[i][j] = True
                # # subsequent "*" and adjacent space in dp is True
                if dp[i][j - 1]:
                    dp[i][j] = True

            # Column 0: must be false, as no string can match a blank pattern
            if j == 0:
                continue  # set to False during setup

            # If string and pattern are matching characters, or is pattern "?"
            if p[j - 1] == string[i - 1] or p[j - 1] == "?":
                dp[i][j] = dp[i - 1][j - 1]

            # If pattern is "*", take a True from an adjacent cell if we can
            elif p[j - 1] == "*":
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return dp[-1][-1]


# true
s = "abcde"
p = "*"
print(patternmatch(s, p))

# true
s = "abcde"
p = "*a?c*"
print(patternmatch(s, p))

# false
s = "abcde"
p = "ad"
print(patternmatch(s, p))

# false
s = "abcde"
p = "ad?"
print(patternmatch(s, p))
