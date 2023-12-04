with open("Day4_input.txt", "r") as file:
    answer = 0

    for i, line in enumerate(file):
        numbersList = line[10:-1].split("|")

        numbersList[0] = numbersList[0].replace("  ", " ").strip()
        numbersList[1] = numbersList[1].replace("  ", " ").strip()

        gameNumbers = numbersList[0].split(" ")
        winningNumbers = set(numbersList[1].split(" "))

        pointValue = 0

        for number in gameNumbers:
            if number in winningNumbers:
                if pointValue == 0:
                    pointValue = 1
                else:
                    pointValue *= 2

        answer += pointValue

print(f"Answer: {answer}")
