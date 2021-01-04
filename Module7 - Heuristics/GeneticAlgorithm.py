import random


def randomList(leftEnd, rightEnd, n):
    return [random.uniform(leftEnd, rightEnd) for number in range(n)]


def styblinskiTang(parametersList):
    result = 0
    for i in range(len(parametersList)):
        result += parametersList[i] ** 4 - 16 * parametersList[i] ** 2 + 5 * parametersList[i]
    return result / 2


def sphere(parametersList):
    result = 0
    for i in range(len(parametersList)):
        result += parametersList[i] ** 2
    return result


def crossover(x1, x2, leftEnd, rightEnd):
    child = []
    for i in range(len(x1)):
        crossing = x1[i] + random.random() * (x2[i] - x1[i])
        crossing = max(min(crossing, rightEnd), leftEnd)
        child.append(crossing)
    return child


def geneticAlgorithm(function, leftEnd, rightEnd, populationSize,
                     mutationProbability, dimension, maximum=False):
    generationCount = 50
    population = [randomList(leftEnd, rightEnd, dimension) for subject in range(populationSize)]

    population.sort(key=lambda x: function(x))
    if maximum:
        population.reverse()

    for t in range(0, generationCount + 1):
        lambdaList = randomList(0, 1, populationSize)
        for subject in range(populationSize):
            if lambdaList[subject] < mutationProbability:
                ksi = random.uniform(-0.5, 0.5)
                for parameter in population[subject]:
                    parameter = max(min(parameter + ksi, rightEnd), leftEnd)

        for subject in range(populationSize - 1):
            population.append(crossover(population[subject], population[subject + 1], leftEnd, rightEnd))

        population.sort(key=lambda x: function(x))
        if maximum:
            population.reverse()
        population = population[:populationSize]

    if maximum:
        print("Maximum of")
    else:
        print("Minimum of")
    result = population[0]
    print(str(function.__name__), "where x =", result[0], "\n f(x) =", function(result), "\n")


geneticAlgorithm(sphere, -10, 10, 100, 0.1, 1)
geneticAlgorithm(sphere, -10, 10, 100, 0.1, 1, True)
geneticAlgorithm(styblinskiTang, -10, 10, 100, 0.1, 1)
geneticAlgorithm(styblinskiTang, -10, 10, 100, 0.1, 1, True)
