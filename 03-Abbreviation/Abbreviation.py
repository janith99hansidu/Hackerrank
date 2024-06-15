def abbreviation(a, b):
    # Initialize the 2D array with dimensions (len(a) + 1) x (len(b) + 1)
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    # Fill the first column with ones
    for i in range(len(a) + 1):
        dp[i][0] = 1

    # Traverse the array row by row, excluding the first row and first column
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            # Check if the letters are the same in a and b, accounting for case
            if a[i - 1].upper() == b[j - 1]:
                if dp[i - 1][j - 1] == 1:
                    dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j]

    # Check if the transformation is possible
    if dp[len(a)][len(b)] == 1:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    print(abbreviation("beFgH", "EFG"))