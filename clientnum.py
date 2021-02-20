import requests
from sys import argv, exit
from time import perf_counter
from math import pi as mathPi

def main(argv):

    if len(argv) != 2:
        print(f'Usage: {argv[0]} <number of steps>')
        exit(1)

    numberOfStepsStr = argv[1]
    try:
        numberOfSteps = int(numberOfStepsStr)
    except:
        print("conversion error")
        exit(-1)

    if numberOfSteps <= 0:
        print('Steps cannot be non-positive.')
        exit(3)

    t1 = perf_counter()

    response = requests.get("http://localhost:3000/pi?numsteps="+ numberOfStepsStr)

    r = response.text

    t2 = perf_counter()

    print(f'Sequential program results with {numberOfStepsStr} steps')
    print(f'Computed pi = {r}')
    print(f'Difference between estimated pi and math.pi = {(abs(float(r) - mathPi))}')
    print('Time to compute = ' + str(t2-t1) + ' seconds')

if __name__ == '__main__':
    main(argv)