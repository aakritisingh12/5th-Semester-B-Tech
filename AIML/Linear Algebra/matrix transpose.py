# Program to find transpose of a matrix
import numpy as np
size = int(input("Enter size of your matrix :"))
mat = [list(map(int, input("Enter row values: ").split())) for i in range(size)]
m = np.array(mat)  # NUMPY ARRAY
print("\n***ORIGINAL MATRIX***")
for row in m:
    print(row)
m2 = []
for i in range(size):
    temp = []
    for j in range(size):
        temp.append(m[j][i])
    m2.append(np.array(temp))
m2 = np.array(m2)
print("\n***TRANSPOSE MATRIX***")
for row in m2:
    print(row)
