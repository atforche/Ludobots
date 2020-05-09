import pyrosim
import matplotlib.pyplot as plt
from robot import ROBOT
from individual import INDIVIDUAL
import random
import copy
import pickle
from population import POPULATION
import constants as c
from Environments import ENVIRONMENTS

envs = ENVIRONMENTS()

parents = POPULATION(c.popSize)
parents.Initialize()
parents.Evaluate(envs, pp=False, pb=True)
parents.Print()

for g in range(c.numGens):
    children = POPULATION(c.popSize)
    children.Fill_From(parents)
    children.Evaluate(envs, pp=False, pb=True)
    children.Print()
    parents = children

for e in range(len(envs.envs)):
    parents.p[0].Start_Evaluation(envs.envs[e], pp=True, pb=False)
    parents.p[0].Compute_Fitness()
