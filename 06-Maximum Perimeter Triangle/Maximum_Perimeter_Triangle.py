def maximumPerimeterTriangle(sticks):
    # Write your code here
    # sort the array in reverse order to pick maximum
    sticks.sort(reverse=True)

    # traverse till end - 2 to get all possible
    for i in range(len(sticks) - 2):
        max_side = sticks[i]
        other_sides = sticks[i + 1] + sticks[i + 2]

        if max_side < other_sides:
            return sticks[i], sticks[i + 1], sticks[i + 2]

    return [-1]


if __name__ == '__main__':
    print(maximumPerimeterTriangle([1, 2, 3]))
