import time
from datetime import datetime

A = [[40, 43, 10, 75],
     [42, 81, 77, 90],
     [85, 22, 73, 19],
     [17, 5, 35, 33]]
B = [[60, 91, 52, 11],
     [7, 58, 70, 11],
     [82, 48, 34, 13],
     [17, 94, 64, 88]]


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


print("Simple nested loops multiplication result")
print(MatrixMultiplication(A, B))

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
