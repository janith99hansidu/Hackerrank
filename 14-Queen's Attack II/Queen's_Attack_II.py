def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    # Directions of queen can move
    squares = 0
    directions = [(1.0, 1.0), (1.0, 0.0), (0.0, 1.0), (1.0, -1.0), (0.0, -1.0), (-1.0, -1.0), (-1.0, 0), (-1.0, 1.0)]

    # iterate trough obstacles and find whether obstacles block queen
    for obj in obstacles:
        try:
            row, column = obj
            row = row - r_q
            column = column - c_q
            # print(row,column)
            # if it removes from the directions that is the squares till that point
            max_num = max(abs(column), abs(row))

            # Divide the number column and row of the max of the numbers to find how many sqares
            find_row = row / max_num
            find_column = column / max_num

            directions.remove((find_row, find_column))
            # print(row, column)

            # update the squares
            squares = squares + int(max(abs(row)-1, abs(column)-1))
            # print(squares)
        except:
            # print("a")
            pass

    print(directions)

    for direction in directions:
        x_move, y_move = direction
        x_center = r_q
        y_center = c_q
        # print(x_center,y_center,"--")
        # while column in range 1.n
        while 1 < x_center < n and 1 < y_center < n:
            x_center = x_center + x_move
            y_center = y_center + y_move
            squares = squares + 1
            # print(x_center,y_center)

    # print(squares)
    return squares


if __name__ == '__main__':
    queensAttack(5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]])
