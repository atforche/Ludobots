import pyrosim

class ROBOT:

    def __init__(self,sim,wt):
        whiteObject = sim.send_cylinder(position=(0,0,0.6), length=1, radius=0.1)
        redObject = sim.send_cylinder(position=(0,0.5,1.05), orientation=(0,1,0), color=(1,0,0), length=1, radius=0.1)
        joint = sim.send_hinge_joint(whiteObject, redObject, (0, 0, 1.05), axis=(-1,0,0), joint_range=(3.14159/2))

        self.T0 = sim.send_touch_sensor(body_id=whiteObject)
        self.SN0 = sim.send_sensor_neuron(sensor_id=self.T0)

        self.M0 = sim.send_rotary_actuator(joint)
        self.MN2 = sim.send_motor_neuron(self.M0)

        sim.send_synapse(source_neuron_id=self.SN0, target_neuron_id=self.MN2, weight=wt)
        self.P4 = sim.send_position_sensor(body_id=redObject)
        self.P5 = sim.send_position_sensor(body_id=redObject, which_dimension='y')
        self.P6 = sim.send_position_sensor(body_id=redObject, which_dimension='z')
