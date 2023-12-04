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

answer = 0

for row in range(ROWS):
    for col in range(COLS):
        if not matrix[row][col] == "*":
            continue

        numSurroundingParts = 0
        visited = set()
        partList = []

        for rowDir, colDir in DIRECTIONS:
            rowPos, colPos = row + rowDir, col + colDir
            if (
                0 <= rowPos < ROWS
                and 0 <= colPos < COLS
                and 48 <= ord(matrix[rowPos][colPos]) <= 57
                and (rowPos, colPos) not in visited
            ):
                numSurroundingParts += 1
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

                partList.append(int(number))

        if numSurroundingParts == 2:
            answer += partList[0] * partList[1]

print(f"answer: {answer}")
