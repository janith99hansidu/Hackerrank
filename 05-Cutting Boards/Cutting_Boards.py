def boardCutting(cost_y, cost_x):
    horizontal_cuts = 0
    vertical_cuts = 0
    cost = 0

    # sort the list to get the maximum
    cost_y.sort(reverse=True)
    cost_x.sort(reverse=True)

    i = 0
    j = 0
    while i < len(cost_y) or j < len(cost_x):

        if i == len(cost_y):
            # if i equal the len(cost_y) print others ending conditions
            # print("x", cost_x[j])

            # calculate the cost
            cost = cost + (vertical_cuts + 1) * cost_x[j]
            horizontal_cuts = horizontal_cuts + 1

            # add one
            j = j + 1
        elif j == len(cost_x):
            # if j equal the len(cost_x) print others ending conditions
            # print("y", cost_y[i])

            # calculate the cost
            cost = cost + (horizontal_cuts + 1) * cost_y[i]
            vertical_cuts = vertical_cuts + 1

            # add one
            i = i + 1
        else:
            # check who is high before ending conditions met
            if cost_y[i] <= cost_x[j]:
                # maximum equal cost x[j]
                # print("x", cost_x[j])

                # calculate the cost
                cost = cost + (vertical_cuts+1)*cost_x[j]
                horizontal_cuts = horizontal_cuts+1

                # add one
                j = j + 1

            else:
                # maximum equal cost y[i]
                # print("y", cost_y[i])

                # calculate the cost
                cost = cost + (horizontal_cuts + 1) * cost_y[i]
                vertical_cuts = vertical_cuts + 1

                # add one
                i = i + 1
    return (cost % (10 ** 9 + 7))


if __name__ == '__main__':
    boardCutting([2, 1, 3, 1, 4], [4, 1, 2])
