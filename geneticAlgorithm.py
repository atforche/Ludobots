import pyrosim
import matplotlib.pyplot as plt
from robot import ROBOT
from individual import INDIVIDUAL
import random
import copy
import pickle
from population import POPULATION

POP_SIZE = 10
parents = POPULATION(POP_SIZE)
parents.Initialize()
parents.Evaluate(True)
parents.Print()

for g in range(200):
    children = POPULATION(POP_SIZE)
    children.Fill_From(parents)
    children.Evaluate(True)
    children.Print()
    parents = children

parents.p[0].Start_Evaluation(False)
parents.p[0].Compute_Fitness()
