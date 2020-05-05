import pyrosim

class ROBOT:

    def __init__(self,sim,wt):
        whiteObject = sim.send_cylinder(position=(0,0,0.6), length=1, radius=0.1)
        redObject = sim.send_cylinder(position=(0,0.5,1.05), orientation=(0,1,0), color=(1,0,0), length=1, radius=0.1)
        joint = sim.send_hinge_joint(whiteObject, redObject, (0, 0, 1.05), axis=(-1,0,0), joint_range=(3.14159/2))

        T0 = sim.send_touch_sensor(body_id=whiteObject)
        SN0 = sim.send_sensor_neuron(sensor_id=T0)

        M0 = sim.send_rotary_actuator(joint)
        MN2 = sim.send_motor_neuron(M0)

        sim.send_synapse(source_neuron_id=SN0, target_neuron_id=MN2, weight=wt)
