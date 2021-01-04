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


def mutateSubject(mutationProbability, population, i, leftEnd, rightEnd):
    temp = population[:i]
    temp.extend(population[(i + 1):])
    mutations = random.sample(temp, 3)
    mutatedSubject = []
    for j in range(len(mutations[0])):
        value = mutations[0][j] + mutationProbability * (mutations[1][j] - mutations[2][j])
        value = max(min(value, rightEnd), leftEnd)
        mutatedSubject.append(value)
    return mutatedSubject


def differentialEvolution(function, leftEnd, rightEnd, populationSize,
                          mutationProbability, crossoverProbability, dimension, maximum=False):
    generationCount = 100
    population = [randomList(leftEnd, rightEnd, dimension) for subject in range(populationSize)]

    for t in range(0, generationCount + 1):
        mutatedSubjects = []
        for i in range(populationSize):
            mutatedSubjects.append(mutateSubject(mutationProbability, population, i, leftEnd, rightEnd))

        crossoveredSubjects = []
        for i in range(populationSize):
            temp = []
            for j in range(dimension):
                r = random.random()
                index = random.randint(0, dimension - 1)
                if r > crossoverProbability and j != index:
                    temp.append(population[i][j])
                else:
                    temp.append(mutatedSubjects[i][j])
            crossoveredSubjects.append(temp)

    population.sort(key=lambda x: function(x))
    if maximum:
        population.reverse()
        print("Maximum of")
    else:
        print("Minimum of")
    result = population[0]
    print(str(function.__name__), "where x =", result[0], "\n f(x) =", function(result), "\n")


differentialEvolution(sphere, -10, 10, 110, 0.1, 0.6, 1)
differentialEvolution(sphere, -10, 10, 110, 0.1, 0.6, 1, True)
differentialEvolution(styblinskiTang, -10, 10, 110, 0.1, 0.6, 1)
differentialEvolution(styblinskiTang, -10, 10, 110, 0.1, 0.6, 1, True)
