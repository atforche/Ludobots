import pyrosim
import matplotlib.pyplot as plt
from robot import ROBOT
from individual import INDIVIDUAL
import random
import copy
import pickle
from population import POPULATION

parents = POPULATION(10)
parents.Evaluate(True)
parents.Print()

for g in range(1,200):
    children = copy.deepcopy(parents)
    children.Mutate()
    children.Evaluate(True)
    parents.ReplaceWith(children)
    print(g)
    parents.Print()

max_index = 0 
max_fitness = 0
for i in range(len(parents.p)):
    if (parents.p[i].fitness > max_fitness):
        max_index = i
        max_fitness = parents.p[i].fitness

parents.p[max_index].Start_Evaluation(False)
parents.p[max_index].Compute_Fitness()