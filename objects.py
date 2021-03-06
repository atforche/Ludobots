import pyrosim

sim = pyrosim.Simulator(play_paused=True, eval_steps=1000)

whiteObject = sim.send_cylinder(position=(0,0,0.6), length=1, radius=0.1)
redObject = sim.send_cylinder(position=(0,0.5,1.05), orientation=(0,1,0), color=(1,0,0), length=1, radius=0.1)

sim.start()
sim.wait_to_finish()