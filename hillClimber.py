import pyrosim
import matplotlib.pyplot as plt
from robot import ROBOT
from individual import INDIVIDUAL
import random
import copy
import pickle

parent = INDIVIDUAL()
parent.Evaluate(True)
print(parent.fitness)

for i in range(100):
    child = copy.deepcopy(parent)
    child.Mutate()
    child.Evaluate(True)
    print('[g:', i,'] [pw:', parent.genome, '] [p:', parent.fitness, '] [c:', child.fitness, ']')
    if (child.fitness > parent.fitness):
        parent = child
        child.Evaluate(False)
        f = open('robot.p', 'wb')
        pickle.dump(parent, f)
        f.close()
