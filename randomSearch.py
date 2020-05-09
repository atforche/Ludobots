import pyrosim
import matplotlib.pyplot as plt
from robot import ROBOT
from individual import INDIVIDUAL
import random

for i in range(5):
    # sim = pyrosim.Simulator(eval_steps=500)
    # robot = ROBOT(sim,random.random()*2 - 1)
    # sim.start()
    # sim.wait_to_finish()

    # x = sim.get_sensor_data(sensor_id=robot.P4)
    # y = sim.get_sensor_data(sensor_id=robot.P5)
    # z = sim.get_sensor_data(sensor_id=robot.P6)
    
    # # plt.plot(x, label="x")
    # # plt.plot(y, label="y")
    # # plt.plot(z, label="z")
    # # plt.legend()
    # # plt.show()
    # print(y[-1])

    individual = INDIVIDUAL()
    individual.Evaluate()
    print(individual.fitness)