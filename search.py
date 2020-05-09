import pyrosim
import matplotlib.pyplot as plt
from robot import ROBOT
import random

for i in range(3):
    sim = pyrosim.Simulator(eval_steps=500)
    robot = ROBOT(sim,random.random()*2 - 1)
    sim.start()
    sim.wait_to_finish()