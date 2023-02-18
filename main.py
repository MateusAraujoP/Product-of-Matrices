A = [[3, 1, 3], [6, 5, 5]]
B = [[100, 50], [50, 100], [50, 50]]

m = len(A)
n = len(A[0])
p = len(B[0])

C = [[0 for j in range(p)] for i in range(m)]

for i in range(m):
    for j in range(p):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]

for row in C:
    print(row)
