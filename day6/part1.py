import time,re, math

def main():
    with open('input.txt') as f:
        lines = f.readlines()


    times = re.findall(r'\d+', lines[0])
    distances = re.findall(r'\d+', lines[1])
    possibleWins = list()
    for i in range(len(times)):
        countWins = 0
        time = int(times[i])
        distance = int(distances[i])
        for j in range(time):
            if (j * (time-j)) > distance:
                countWins+=1
        possibleWins.append(countWins)
    return math.prod(possibleWins)

if __name__ == '__main__':
    x = time.perf_counter_ns()
    answer = main()
    y = time.perf_counter_ns()
    print('Answer:', answer)
    print('Time (ms):', (y-x)/1000)
