with open("Day4_input.txt", "r") as file:
    answer = 0
    numCards = [1] * 198

    for i, line in enumerate(file):
        numbersList = line[10:-1].split("|")

        numbersList[0] = numbersList[0].replace("  ", " ").strip()
        numbersList[1] = numbersList[1].replace("  ", " ").strip()

        gameNumbers = numbersList[0].split(" ")
        winningNumbers = set(numbersList[1].split(" "))

        numMatches = 0
        answer += numCards[i]

        for number in gameNumbers:
            if number in winningNumbers:
                numMatches += 1

        for j in range(1, numMatches + 1):
            if i + j < 198:
                numCards[i + j] += numCards[i]

print(f"Answer: {answer}")
