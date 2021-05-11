# Author: Timothy Jan
# Date: 04/26/2021
# Description: Figures out how many dogs we can feed given dog hunger levels and dog biscuits. The same biscuit
#              cannot got to two dogs and each dog only gets one biscuit.


def feedDog(hunger_level, biscuit_size):
    """Determines how many hungry pooches we can feed given their hunger level and biscuit sizes."""
    count = 0
    remaining_biscuits = biscuit_size.copy()
    for i in range(len(hunger_level)):
        for j in range(len(remaining_biscuits)):
            if hunger_level[i] <= remaining_biscuits[j]:
                count += 1
                remaining_biscuits.remove(remaining_biscuits[j])
                break
    return count


# [hunger] [biscuits]
print(feedDog([1, 2, 3], [1, 1]))  # 1
print(feedDog([1, 2], [1, 2, 3]))  # 2
print(feedDog([1, 1, 1], [1, 1]))  # 2
print(feedDog([1, 1], [4, 5]))  # 2
print(feedDog([4, 4, 4], [0, 1, 2, 3]))  # 0
