import pyrosim
import matplotlib.pyplot as plt
from robot import ROBOT
from individual import INDIVIDUAL
import random
import copy
import pickle
from population import POPULATION

parents = POPULATION(5)
parents.Evaluate(True)
parents.Print()

for g in range(1,10):
    children = copy.deepcopy(parents)
    children.Mutate()
    children.Evaluate(True)
    parents.ReplaceWith(children)
    print(g)
    parents.Print()