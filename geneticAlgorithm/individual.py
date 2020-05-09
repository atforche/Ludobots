import random
import math
import pyrosim
from robot import ROBOT
import numpy
import constants as c

class INDIVIDUAL:

    def __init__(self, i):
        self.genome = numpy.random.rand(5,8) * 2 - 1
        self.fitness = 0
        self.ID = i

    # def Evaluate(self, pb):
    #     self.Start_Evaluation(pb)
    #     self.Compute_Fitness()
        

    def Start_Evaluation(self, env, pp, pb):
        self.sim = pyrosim.Simulator(eval_steps=c.evalTime, play_blind=pb, play_paused=pp)
        self.robot = ROBOT(self.sim, self.genome)
        env.Send_To(self.sim)
        self.sim.start()

    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        y = self.sim.get_sensor_data(sensor_id=self.robot.L4)
        self.fitness += y[-1]
        del self.sim


    def Mutate(self):
        mutationProb = 0.05
        for i in range(len(self.genome)):
            for j in range(len(self.genome[0])):
                roll = random.random()
                if roll < mutationProb:
                    self.genome[i][j] = random.gauss(self.genome[i][j], math.fabs(self.genome[i][j]))
        
        # if self.genome[rowToMutate][colToMutate] > 1:
        #     self.genome[rowToMutate][colToMutate] = 1
        # elif self.genome[rowToMutate][colToMutate] < -1:
        #     self.genome[rowToMutate][colToMutate] = -1

    def Print(self):
        print('[', self.ID, '] [', self.fitness, ']')