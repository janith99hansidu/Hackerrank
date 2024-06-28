def climbingLeaderboard(ranked, player):
    # Write your code here

    # make a ranked list to store the rank of initial ranked
    return_list = []
    ranked_list = []
    rank = 1
    ranked_list.append(1)  # add first element as it always is first

    # add elements from the 2nd item in the ranked list
    for i in range(1, len(ranked)):
        if ranked[i] == ranked[i - 1]:
            ranked_list.append(rank)
        else:
            rank = rank + 1
            ranked_list.append(rank)

    # give element to the last position at first
    rank_given = ranked_list[len(ranked) - 1]

    for j in range(len(player)):
        # iterate from the last element to find the correct place
        i = len(ranked) - 1
        while ranked[i] <= player[j]:
            rank_given = ranked_list[i] - 1
            if i == 0:
                break
            i = i - 1

        # add one to the rank_given otherwise it is not same as the i element
        if ranked[i] == player[j]:
            rank_given = ranked_list[i]
        else:
            rank_given = rank_given + 1

        #print(rank_given)
        return_list.append(rank_given)

    return return_list


if __name__ == '__main__':
    climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120])
    # 6
    # 4
    # 2
    # 1
    climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102])
    # 6
    # 5
    # 4
    # 2
    # 1
