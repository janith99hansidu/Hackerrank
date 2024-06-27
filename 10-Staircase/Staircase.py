def staircase(n):
    # Write your code here
    for i in range(0, n):
        print(' ' * (n - i - 1) + '#' * (i + 1))


if __name__ == '__main__':
    staircase(2)
    staircase(5)