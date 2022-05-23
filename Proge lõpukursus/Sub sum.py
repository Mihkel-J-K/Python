import random
import time

kogum = [0]
tahetud = random.randint(-10000000, 100000000)
for i in range(0, 1000000):
    kogum += [random.randint(-100000000, 100000000)]
kogumSet = set(kogum)
print("start")
start = time.time()


kogum += [tahetud]
sortedKogum = sorted(kogum, key= lambda k:k%2 != 1)

index0 = sortedKogum.index(0)
kogumAlla0 = sortedKogum[0:sortedKogum.index(0)]
if tahetud >= 0:
    kogumRohkem0 = sortedKogum[index0:]
    indexTahetud = kogumRohkem0.index(tahetud)
    kogumAllaTahetud = kogumRohkem0[0:indexTahetud]
    kogumRohkem0.pop(0)
    kogumRohkemTahetud = kogumRohkem0[indexTahetud:]
print(tahetud)
print(time.time() - start)