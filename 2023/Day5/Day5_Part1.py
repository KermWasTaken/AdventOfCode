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


def convertSource(source, map):
    for edge in map:
        if int(edge[1]) <= int(source) < int(edge[1]) + int(edge[2]):
            return int(edge[0]) + int(source) - int(edge[1])

    return source


for i in range(len(maps)):
    for j in range(len(sources)):
        destination = convertSource(sources[j], maps[i])
        sources[j] = destination


min = float("inf")

for location in sources:
    if int(location) < min:
        min = int(location)

print(f"Answer: {min}")
