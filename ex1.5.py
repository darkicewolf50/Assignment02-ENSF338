import timeit
from matplotlib import pyplot as plt

def OnComplex(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    else:
        memo[n] = OnComplex(n-1, memo) + OnComplex(n-2, memo)
        return memo[n]

def O2nComplex(n):
    if n == 0 or n == 1:
        return n
    else:
        return O2nComplex(n-1) + O2nComplex(n-2)

if __name__ == "__main__":
    To_test = [i for i in range(36)]
    listtimeOn = []
    listtimeO2n = []
    for j in To_test:
        timeOn = timeit.timeit(lambda: OnComplex(j), globals={'j' : j}, number=1)
        timeO2n = timeit.timeit(lambda: O2nComplex(j), globals={'j' : j}, number=1)
        listtimeOn.append(timeOn)
        listtimeO2n.append(timeO2n)

    plt.plot(listtimeOn, label= 'OnComplex')
    plt.plot(listtimeO2n, label = 'O2nComplex')
    plt.legend()

    plt.show()


