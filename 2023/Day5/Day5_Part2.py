with open("Day5_input.txt", "r") as file:
    data = file.read()

lines = data.split("\n")
sources = lines[0][7:].split(" ")

seedToSoil = []

for i in range(3, 20):
    seedToSoil.append(lines[i].split(" "))

soilToFertilizer = []

for i in range(22, 53):
    soilToFertilizer.append(lines[i].split(" "))

fertilizerToWater = []

for i in range(55, 94):
    fertilizerToWater.append(lines[i].split(" "))

waterToLight = []

for i in range(96, 113):
    waterToLight.append(lines[i].split(" "))

lightToTemperature = []

for i in range(115, 134):
    lightToTemperature.append(lines[i].split(" "))

temperatureToHumidity = []

for i in range(136, 166):
    temperatureToHumidity.append(lines[i].split(" "))

humidityToLocation = []

for i in range(168, 206):
    humidityToLocation.append(lines[i].split(" "))


maps = [
    seedToSoil,
    soilToFertilizer,
    fertilizerToWater,
    waterToLight,
    lightToTemperature,
    temperatureToHumidity,
    humidityToLocation,
]

# Take an ending location, find the seed that arrives at that location, check if seed is valid
# I want to map ending location (Starting at lowest) to its seed. Once I find a valid seed, break out of function

# Maps: (Destination Start, Source Start, Range)


def findSourceSeed(startingLocation, maps):
    if not maps:
        return startingLocation

    for edge in maps[-1]:
        if int(edge[0]) <= startingLocation < int(edge[0]) + int(edge[2]):
            return findSourceSeed(
                int(edge[1]) + startingLocation - int(edge[0]), maps[:-1]
            )

    return findSourceSeed(startingLocation, maps[:-1])


def isValidSeed(seed):
    for i in range(len(sources) // 2):
        if (
            int(sources[2 * i])
            <= seed
            < (int(sources[2 * 1]) + int(sources[2 * i + 1]))
        ):
            return True

    return False


startingLocation = 0

while True:
    print(f"Starting location: {startingLocation}")
    sourceSeed = findSourceSeed(startingLocation, maps)
    if isValidSeed(sourceSeed):
        print(f"Answer: {startingLocation}")
        break
    startingLocation += 1
