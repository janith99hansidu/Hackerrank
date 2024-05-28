def recursion(n):
    if n == 1:
        return 1
    else:
        return n * recursion(n - 1)


def extraLongFactorials(n):
    # Write your code here
    print(recursion(n))


if __name__ == '__main__':
    n = int(input().strip())
    extraLongFactorials(n)