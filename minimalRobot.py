import pyrosim

class ROBOT:

    def __init__(self,sim,wts):
        whiteObject = sim.send_cylinder(position=(0,0,0.6), length=1, radius=0.1)
        redObject = sim.send_cylinder(position=(0,0.5,1.05), orientation=(0,1,0), color=(1,0,0), length=1, radius=0.1)
        joint = sim.send_hinge_joint(whiteObject, redObject, (0, 0, 1.05), axis=(-1,0,0), joint_range=(3.14159/2))

        self.T0 = sim.send_touch_sensor(body_id=whiteObject)
        self.SN0 = sim.send_sensor_neuron(sensor_id=self.T0)

        self.T1 = sim.send_touch_sensor(body_id=redObject)
        self.SN1 = sim.send_sensor_neuron(sensor_id=self.T1)

        self.P2 = sim.send_position_sensor(body_id=whiteObject, which_dimension='z')
        self.SN2 = sim.send_sensor_neuron(sensor_id=self.P2)

        ray = sim.send_ray(redObject, (0,1.1,1.1), (0,1,0))
        self.R3 = sim.send_ray_sensor(ray)
        self.SN3 = sim.send_sensor_neuron(sensor_id=self.R3)

        self.M0 = sim.send_rotary_actuator(joint)
        self.MN2 = sim.send_motor_neuron(self.M0)

        sensorNeurons = {}
        sensorNeurons[0] = self.SN0
        sensorNeurons[1] = self.SN1
        sensorNeurons[2] = self.SN2
        sensorNeurons[3] = self.SN3

        motorNeurons = {}
        motorNeurons[0] = self.MN2

        for s in sensorNeurons:
            for m in motorNeurons:
                sim.send_synapse(source_neuron_id=sensorNeurons[s], target_neuron_id=motorNeurons[m], weight=wts[s])
        # self.P4 = sim.send_position_sensor(body_id=redObject)
        self.P5 = sim.send_position_sensor(body_id=redObject, which_dimension='y')
        # self.P6 = sim.send_position_sensor(body_id=redObject, which_dimension='z')
