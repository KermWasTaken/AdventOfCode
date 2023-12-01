class Node:
    def __init__(self):
        self.next = {}


rootForward = Node()
rootBackward = Node()


def buildTrie(word, currRoot, i):
    currNode = currRoot
    while word:
        if word[0] not in currNode.next:
            currNode.next[word[0]] = Node()

        currNode = currNode.next[word[0]]
        word = word[1:]
    currNode.next = str(i)


numbers = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

reverseNumbers = (
    "eno",
    "owt",
    "eerht",
    "ruof",
    "evif",
    "xis",
    "neves",
    "thgie",
    "enin",
)

for i, number in enumerate(numbers):
    buildTrie(number, rootForward, i + 1)

for i, number in enumerate(reverseNumbers):
    buildTrie(number, rootBackward, i + 1)

totalSum = 0

with open("Day1_input.txt", "r") as file:
    for line in file:
        l, r = 0, len(line) - 1

        found = False
        while l < len(line) and not found:
            if 48 <= ord(line[l]) <= 57:
                first = line[l]
                break

            if line[l] in rootForward.next:
                currNode = rootForward.next[line[l]]
                temp = l + 1
                while temp < len(line) and line[temp] in currNode.next:
                    currNode = currNode.next[line[temp]]
                    if type(currNode.next) == str:
                        first = currNode.next
                        found = True
                        break
                    temp += 1
            l += 1

        found = False
        while r > -1 and not found:
            if 48 <= ord(line[r]) <= 57:
                last = line[r]
                break

            if line[r] in rootBackward.next:
                currNode = rootBackward.next[line[r]]
                temp = r - 1
                while temp > -1 and line[temp] in currNode.next:
                    currNode = currNode.next[line[temp]]
                    if type(currNode.next) == str:
                        last = currNode.next
                        found = True
                        break
                    temp -= 1
            r -= 1

        print(int(first + last))
        totalSum += int(first + last)

print(totalSum)
