# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

A = np.array([int(i) for i in raw_input().split()])
B = np.array([int(i) for i in raw_input().split()])

print np.inner(A, B)
print np.outer(A, B)
