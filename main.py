import math

base = 2
t = 0
f = 1
step = 0.000001
numToGenerate = 11

fAtIntegers = []
k = math.log(base)
for i in range(int(1/step)*numToGenerate):
    t += step
    f += step * (f * k)
    if (i % int(1/step) == 0):
        fAtIntegers.append(round(f))
print(fAtIntegers)
