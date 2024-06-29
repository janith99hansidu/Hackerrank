def nonDivisibleSubset(k, s):
    non_divisible = []
    # get the first pair that is not divisible
    i = 0
    while i < len(s) - 2:
        if (s[i] + s[i + 1]) % k != 0:
            non_divisible.append(s[i])
            non_divisible.append(s[i + 1])
            break
        i = i + 1

    # add one by one from the remaining elements
    while i < len(s) - 2:
        can_add = True
        # get the next element s[i+2]
        for j in range(len(non_divisible)):
            if (non_divisible[j] + s[i + 2]) % k == 0:
                can_add = False
                break

        # the number can add to the non_divisible add it
        if not can_add:
            pass
        else:
            non_divisible.append(s[i + 2])

        i = i + 1

    return len(non_divisible)


if __name__ == '__main__':
    nonDivisibleSubset(3, [1, 7, 2, 4])
