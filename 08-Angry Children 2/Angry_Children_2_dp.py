def angryChildren(k, packets):
    n = len(packets)

    # Sort the packets
    packets.sort()

    # Calculate prefix sums
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + packets[i]

    # Calculate initial unfairness
    result = 0
    dp = 0
    for j in range(1, k):
        dp += j * (packets[j] - packets[j - 1])
        result += dp

    # Sliding window to find the minimum unfairness
    previous = result
    for i in range(1, n - k + 1):
        previous += -2 * (prefix_sums[i + k - 1] - prefix_sums[i]) + (k - 1) * (packets[i + k - 1] + packets[i - 1])
        result = min(result, previous)

    return result
