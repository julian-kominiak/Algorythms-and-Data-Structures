import random
import math


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


def fly(startingNest, leftEnd, rightEnd):
    newNest = startingNest[:]
    for i in range(10):
        cuckoo = random.randint(0, len(startingNest) - 1)
        newNest[cuckoo] += random.normalvariate(0, 1) * 0.01
        newNest[cuckoo] = max(min(newNest[cuckoo], rightEnd), leftEnd)
    return newNest


def cuckooSearch(function, leftEnd, rightEnd, numberOfNests, adoptionProbability, dimension, maximum=False):
    generationCount = 100
    nests = [randomList(leftEnd, rightEnd, dimension) for nest in range(numberOfNests)]

    for t in range(0, generationCount + 1):
        startingNestIndex = random.randint(0, numberOfNests - 1)
        startingNest = nests[startingNestIndex]
        newNest = fly(startingNest, leftEnd, rightEnd)
        if maximum:
            if function(newNest) < function(startingNest) and random.random() < adoptionProbability:
                nests[startingNestIndex] = newNest
        else:
            if function(newNest) > function(startingNest) and random.random() < adoptionProbability:
                nests[startingNestIndex] = newNest
        nests.sort(key=lambda x: function(x))
        if maximum:
            nests.reverse()
        nests = nests[:(numberOfNests//2)]
        newNests = [randomList(leftEnd, rightEnd, dimension) for nest in range(numberOfNests - len(nests) + 1)]
        nests.extend(newNests)

    if maximum:
        print("Maximum of")
    else:
        print("Minimum of")
    result = nests[0]
    print(str(function.__name__), "where x =", result[0], "\n f(x) =", function(result), "\n")


cuckooSearch(sphere, -10, 10, 10, 0.6, 1)
cuckooSearch(sphere, -10, 10, 10, 0.6, 1, True)
cuckooSearch(styblinskiTang, -10, 10, 10, 0.6, 1)
cuckooSearch(styblinskiTang, -10, 10, 10, 0.6, 1, True)
