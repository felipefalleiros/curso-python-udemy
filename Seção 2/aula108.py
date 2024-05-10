# count interador sem fim
from itertools import count

c1 = count(10, 8) #10 inicio, 8 step, como foi dito count nao tem fim
r1 = range(10, 100, 8) #10 inicio, 100 fim, 8 step

print('c1', hasattr(c1, "__iter__"))
print('c1', hasattr(c1, "__next__"))
print('Count')
for i in c1:
    if i >= 100:
        break
    print(i)

print()
print('Range')
for i in r1:
    print(i)
