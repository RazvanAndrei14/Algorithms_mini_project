import time
from datetime import datetime

A = [[4023123, 43432578, 16516280, 74464575],
     [4871142, 81231546, 77848897, 90541889],
     [8554658, 22656545, 73165468, 19165465],
     [1721321, 58972165, 35654654, 33546541],
     [8554658, 22656545, 73165468, 19165465],
     [1721321, 58972165, 35654654, 33546541],
     [1721321, 58972165, 35654654, 33546541],
     [7156487, 58554654, 70165465, 11546545]]
B = [[6021546, 91648849, 52654689, 11564544],
     [7156487, 58554654, 70165465, 11546545],
     [8254545, 48556465, 34132879, 13215468],
     [1765468, 94455458, 64546587, 88565464],
     [8554658, 22656545, 73165468, 19165465],
     [1721321, 58972165, 35654654, 33546541],
     [8554658, 22656545, 73165468, 19165465],
     [1721321, 58972165, 35654654, 33546541]]


# Classic matrix multiplication with nested loops
def MatrixMultiplication(first_matrix, second_matrix):
    results = []
    try:
        for i in range(len(first_matrix)):
            rows = []
            for j in range(len(second_matrix[0])):
                item = 0
                for k in range(len(first_matrix[0])):
                    item += first_matrix[i][k] * second_matrix[k][j]
                rows.append(item)
            results.append(rows)
            return results
    except:
        return "These matrices aren't squared."


# print("Simple nested loops multiplication result")
# print(MatrixMultiplication(A, B))

allRunningTimes = []
allStartTimes = []
allEndTimes = []
nrOfIterations = 100000
for i in range(nrOfIterations):
    start_time = datetime.now()
    MatrixMultiplication(A, B)
    end_time = datetime.now()
    allStartTimes.append(start_time)
    allEndTimes.append(end_time)

timeLapsed = allEndTimes[nrOfIterations - 1] - allStartTimes[0]

print('Started: {}'.format(allStartTimes[0]) + ' Ended: {}'.format(allEndTimes[nrOfIterations - 1]), sep="\n")
print('Time lapsed: {}'.format(timeLapsed))
print('Average time/iteration: {}'.format(timeLapsed / nrOfIterations))
