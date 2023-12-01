totalSum = 0

with open("Day1_input.txt", "r") as file:
    for line in file:
        currSum = 0
        l, r = 0, len(line) - 1
        while not (48 <= ord(line[l]) <= 57):
            l += 1
        while not (48 <= ord(line[r]) <= 57):
            r -= 1

        totalSum += int(line[l] + line[r])

print(totalSum)
