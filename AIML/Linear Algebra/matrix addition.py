# Program to add two matrices using nested loop
import numpy as np
size = int(input("Enter size of your matrix :"))
print("\n******Matrix 1******")
m1 = [list(map(int, input("Enter row values: ").split())) for i in range(size)]
print("\n******Matrix 2******")
m2 = [list(map(int, input("Enter row values: ").split())) for i in range(size)]
m1 = np.array(m1)
m2 = np.array(m2)
m3 = []
for i in range(size):
    temp = []
    for j in range(size):
        temp.append(m1[i][j]+m2[i][j])
    m3.append(np.array(temp))
m3 = np.array(m3)
print("\n----After addition----")
for row in m3:
    print(row)