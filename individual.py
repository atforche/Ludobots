import random
import math
import pyrosim
from robot import ROBOT
import numpy

class INDIVIDUAL:

    def __init__(self, i):
        self.genome = numpy.random.rand(4,8) * 2 - 1
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
        rowToMutate = random.randint(0,len(self.genome)-1)
        colToMutate = random.randint(0,len(self.genome[0])-1)
        self.genome[rowToMutate][colToMutate] = random.gauss(self.genome[rowToMutate][colToMutate], math.fabs(self.genome[rowToMutate][colToMutate]))
        if self.genome[rowToMutate][colToMutate] > 1:
            self.genome[rowToMutate][colToMutate] = 1
        elif self.genome[rowToMutate][colToMutate] < -1:
            self.genome[rowToMutate][colToMutate] = -1

    def Print(self):
        print('[', self.ID, '] [', self.fitness, ']')