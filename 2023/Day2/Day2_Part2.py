colorIndices = {"r": 0, "g": 1, "b": 2}
sumPowers = 0

with open("Day2_input.txt") as file:
    for line in file:
        lineElements = line.split(":")[1]
        rounds = lineElements.split(";")
        print(rounds)
        maxOfRGB = [0, 0, 0]
        for round in rounds:
            parsedRound = round.strip().split(" ")
            for i in range(len(parsedRound)):
                if not i % 2:
                    if (
                        int(parsedRound[i])
                        > maxOfRGB[colorIndices[parsedRound[i + 1][0]]]
                    ):
                        maxOfRGB[colorIndices[parsedRound[i + 1][0]]] = int(
                            parsedRound[i]
                        )

        sumPowers += maxOfRGB[0] * maxOfRGB[1] * maxOfRGB[2]

print(sumPowers)
