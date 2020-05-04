import pyrosim
import matplotlib.pyplot as plt

sim = pyrosim.Simulator(play_paused=True,eval_steps=1000)

whiteObject = sim.send_cylinder(position=(0,0,0.6), length=1, radius=0.1)
redObject = sim.send_cylinder(position=(0,0.5,1.05), orientation=(0,1,0), color=(1,0,0), length=1, radius=0.1)
joint = sim.send_hinge_joint(whiteObject, redObject, (0, 0, 1.05), axis=(-1,0,0), joint_range=(3.14159/2))

T0 = sim.send_touch_sensor(body_id=whiteObject)
T1 = sim.send_touch_sensor(body_id=redObject)
P2 = sim.send_proprioceptive_sensor(joint_id=joint)
ray = sim.send_ray(redObject, (0,1.1,1.1), (0,1,0))
R3 = sim.send_ray_sensor(ray)

SN0 = sim.send_sensor_neuron(sensor_id=T0)
SN1 = sim.send_sensor_neuron(sensor_id=T1)

M0 = sim.send_rotary_actuator(joint)
MN2 = sim.send_motor_neuron(M0)

sim.send_synapse(source_neuron_id=SN1, target_neuron_id=MN2, weight=-1.0)
sim.send_synapse(source_neuron_id=SN0, target_neuron_id=MN2, weight=-1)

sim.start()
sim.wait_to_finish()
sensorData = sim.get_sensor_data(sensor_id=P2)

f = plt.figure()
panel = f.add_subplot(111)
plt.plot(sensorData)
plt.show()