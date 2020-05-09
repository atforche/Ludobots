import pyrosim

sim = pyrosim.Simulator(play_paused=True, eval_steps=1000)

whiteObject = sim.send_cylinder(position=(0,0,0.6), length=1, radius=0.1)
redObject = sim.send_cylinder(position=(0,0.5,1.05), orientation=(0,1,0), color=(1,0,0), length=1, radius=0.1)
joint = sim.send_hinge_joint(whiteObject, redObject, (0, 0, 1.05), axis=(-1,0,0), joint_range=(3.14159/2))

sim.start()
sim.wait_to_finish()