# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n=int(input())
a = numpy.array([input().split() for _ in range(n)],int)
b = numpy.array([input().split() for _ in range(n)],int)
m = numpy.dot(a,b)
print (m)
