import numpy as np

with open ("15/inputs.txt") as f:
    inp = f.readlines()

inp[:] = [[int(num) for num in line.strip("\n")] for line in inp]

start = (0, 0)
end = (len(inp) - 1, len(inp[-1]) - 1)

R, C = end[0] + 1, end[1] + 1
print(R, C)

cost = [[0 for x in range(5 * R)] for x in range(5 * C)]

for i in range(R):
    for j in range(C):
        c = inp[i][j]
        for k in range(5):
            for m in range(5):
                if k + m + c <= 9:
                    cost[i + R * k][j + C * m] = c + k + m
                else:
                    cost[i + R * k][j + C * m] = c + k + m - 9
                

def minCost(cost, m, n):
 
    # Instead of following line, we can use int tc[m+1][n+1] or
    # dynamically allocate memoery to save space. The following
    # line is used to keep te program simple and make it working
    # on all compilers.
    tc = [[0 for x in range(C)] for x in range(R)]
 
    tc[0][0] = 0
 
    # Initialize first column of total cost(tc) array
    for i in range(1, m+1):
        tc[i][0] = tc[i-1][0] + cost[i][0]
 
    # Initialize first row of tc array
    for j in range(1, n+1):
        tc[0][j] = tc[0][j-1] + cost[0][j]
 
    # Construct rest of the tc array
    for i in range(1, m+1):
        for j in range(1, n+1):
            tc[i][j] = min(tc[i-1][j], tc[i][j-1]) + cost[i][j]
 
    return tc[m][n]

R, C = len(cost), len(cost[-1])
print(R, C)

print(minCost(cost, R - 1, C - 1) - 2) #-2?????????????
# print(len(cost[1]))
# for i in cost:
#     print(i)
