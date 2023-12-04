import copy

matrix = []

with open("Day3_input.txt", "r") as file:
    for line in file:
        temp = []
        for character in line:
            temp.append(character)
        matrix.append(copy.deepcopy(temp[:-1]))


ROWS = len(matrix)
COLS = len(matrix[0])
DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1))

visited = set()

answer = 0

for row in range(ROWS):
    for col in range(COLS):
        if matrix[row][col] == "." or 48 <= ord(matrix[row][col]) <= 57:
            continue

        for rowDir, colDir in DIRECTIONS:
            rowPos, colPos = row + rowDir, col + colDir
            if (
                0 <= rowPos < ROWS
                and 0 <= colPos < COLS
                and 48 <= ord(matrix[rowPos][colPos]) <= 57
                and (rowPos, colPos) not in visited
            ):
                visited.add((rowPos, colPos))
                number = matrix[rowPos][colPos]
                l, r = colPos - 1, colPos + 1

                while l >= 0 and 48 <= ord(matrix[rowPos][l]) <= 57:
                    number = matrix[rowPos][l] + number
                    visited.add((rowPos, l))
                    l -= 1

                while r < COLS and 48 <= ord(matrix[rowPos][r]) <= 57:
                    number = number + matrix[rowPos][r]
                    visited.add((rowPos, r))
                    r += 1

                answer += int(number)

print(f"answer: {answer}")
