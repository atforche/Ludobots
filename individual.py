import random
import math
import pyrosim
from robot import ROBOT
import numpy

class INDIVIDUAL:

    def __init__(self, i):
        self.genome = numpy.random.rand(4) * 2 - 1
        self.fitness = 0
        self.ID = i

    # def Evaluate(self, pb):
    #     self.Start_Evaluation(pb)
    #     self.Compute_Fitness()
        

    def Start_Evaluation(self, pb):
        self.sim = pyrosim.Simulator(eval_steps=500, play_blind=pb)
        self.robot = ROBOT(self.sim, self.genome)
        self.sim.start()

    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        y = self.sim.get_sensor_data(sensor_id=self.robot.P5)
        self.fitness = y[-1]
        del self.sim


    def Mutate(self):
        geneToMutate = random.randint(0,3)
        self.genome[geneToMutate] = random.gauss(self.genome[geneToMutate], math.fabs(self.genome[geneToMutate]))

    def Print(self):
        print('[', self.ID, '] [', self.fitness, ']')