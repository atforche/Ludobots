import random
import math
import pyrosim
from robot import ROBOT

class INDIVIDUAL:

    def __init__(self):
        self.genome = random.random() * 2 - 1
        self.fitness = 0

    def Evaluate(self, pb):
        sim = pyrosim.Simulator(eval_steps=500, play_blind=pb)
        robot = ROBOT(sim, self.genome)
        sim.start()
        sim.wait_to_finish()

        # x = sim.get_sensor_data(sensor_id=robot.P4)
        y = sim.get_sensor_data(sensor_id=robot.P5)
        # z = sim.get_sensor_data(sensor_id=robot.P6)
        
        # plt.plot(x, label="x")
        # plt.plot(y, label="y")
        # plt.plot(z, label="z")
        # plt.legend()
        # plt.show()
        # print(y[-1])
        self.fitness = y[-1]

    def Mutate(self):
        self.genome = random.gauss(self.genome, math.fabs(self.genome))