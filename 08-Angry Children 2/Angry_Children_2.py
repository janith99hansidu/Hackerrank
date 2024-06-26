# brute force implementation
def angryChildren(k, packets):
    # Write your code here
    # sort the array
    packets.sort()
    # print(packets)

    temp_sum = 0
    min_sum = 10 ** 10

    # one iteration
    for l in range(0,len(packets) - k):
        # print(l)
        for i in range(l, k + l):
            for j in range(i + 1, k + l):
                # print(packets[i], packets[j])
                temp_sum = temp_sum + packets[j] - packets[i]

        if min_sum > temp_sum:
            min_sum = temp_sum
        # one iteration end
        # print(min_sum)

    return min_sum


if __name__ == '__main__':
    angryChildren(4, [10, 4, 1, 2, 3, 4, 10, 20, 30, 40, 100, 200])
