# https://www.facebook.com/abhi.sensharma/posts/1241788872853419
# Subscribed by Abhishek Sharma

import numpy
n,m = map(int,input().split())
ar = []
for i in range(n):
    row = list(map(int,input().split()))
    ar.append(row)

np_ar = numpy.array(ar)
print(numpy.transpose(np_ar))
print(np_ar.flatten())
