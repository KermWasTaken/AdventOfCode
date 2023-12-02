numCubes = {"r": 12, "b": 14, "g": 13}
sumID = 0

with open("Day2_input.txt") as file:
    for idx, line in enumerate(file):
        lineElements = line.split(":")[1]
        rounds = lineElements.split(";")
        print(rounds)
        for round in rounds:
            isValid = True
            parsedRound = round.strip().split(" ")
            for i in range(len(parsedRound)):
                if not i % 2:
                    if int(parsedRound[i]) > numCubes[parsedRound[i + 1][0]]:
                        isValid = False
                        break

            if not isValid:
                break

        if isValid:
            sumID += idx + 1


print(sumID)
