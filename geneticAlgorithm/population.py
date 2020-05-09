from individual import INDIVIDUAL
import copy
import random
from Environments import ENVIRONMENTS

class POPULATION:

    def __init__(self, popSize):
        self.p = {}
        self.popSize = popSize
        

    def Initialize(self):
        for i in range(self.popSize):
            self.p[i] = INDIVIDUAL(i)

    def Print(self):
        for i in self.p:
            if (i in self.p):
                self.p[i].Print()
        print()

    def Evaluate(self, envs, pp=False, pb=True):
        for i in self.p:
            self.p[i].fitness = 0
        for e in range(len(envs.envs)):
            for i in self.p:
                self.p[i].Start_Evaluation(envs.envs[e], pp,pb)
            for i in self.p:
                self.p[i].Compute_Fitness()
        for i in self.p:
            self.p[i].fitness = self.p[i].fitness / 4

    def Mutate(self):
        for i in self.p:
            self.p[i].Mutate()

    def ReplaceWith(self,other):
        for i in self.p:
            if (self.p[i].fitness < other.p[i].fitness):
                self.p[i] = other.p[i]

    def Copy_Best_From(self, other):
        max_fitness = float('-inf')
        max_index = -1
        for i in range(len(other.p)):
            if other.p[i].fitness > max_fitness:
                max_fitness = other.p[i].fitness
                max_index = i
        self.p[0] = copy.deepcopy(other.p[max_index])

    def Collect_Children_From(self,other):
        for i in range(1,self.popSize):
            winner = other.Winner_Of_Tournament_Selection()
            self.p[i] = copy.deepcopy(winner)
            self.p[i].Mutate()

    def Winner_Of_Tournament_Selection(other):
        p1 = random.randint(0,len(other.p)-1)
        p2 = random.randint(0,len(other.p)-1)
        while p1 == p2:
            p2 = random.randint(0,len(other.p)-1)
        if other.p[p1].fitness > other.p[p2].fitness:
            return other.p[p1]
        else:
            return other.p[p2]

    def Fill_From(self, other):
        self.Copy_Best_From(other)
        self.Collect_Children_From(other)
        self.Print()