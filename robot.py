import pyrosim
import constants as c
import random

class ROBOT:

    def __init__(self,sim,wts):
        
        self.send_objects(sim)
        self.send_joints(sim)
        self.send_sensors(sim)
        self.send_neurons(sim)
        self.send_synapses(sim,wts)

        del self.O
        del self.J
        del self.S
        del self.SN
        del self.MN
        
    def send_objects(self,sim):
        # self.whiteObject = sim.send_cylinder(position=(0,0,0.6), length=1, radius=0.1)
        # self.redObject = sim.send_cylinder(position=(0,0.5,1.05), orientation=(0,1,0), color=(1,0,0), length=1, radius=0.1)
        self.O0 = sim.send_box(position=(0,0,c.L + c.R), sides=(c.L,c.L,2*c.R), color=(0.5,0.5,0.5))
        self.O1 = sim.send_cylinder(position=(0, c.L, c.L + c.R), length = c.L, radius=c.R, orientation=(0,1,0),color=(1,0,0))
        self.O2 = sim.send_cylinder(position=(c.L, 0, c.L + c.R), orientation=(1,0,0), length=c.L, radius=c.R, color=(0,1,0))
        self.O3 = sim.send_cylinder(position=(0,-c.L,c.L+c.R), orientation=(0,-1,0), length=c.L, radius=c.R, color=(0,0,1))
        self.O4 = sim.send_cylinder(position=(-c.L,0,c.L+c.R), orientation=(-1,0,0), length=c.L, radius=c.R, color=(1,0,1))
        self.O5 = sim.send_cylinder(position=(0,1.5*c.L,(c.L+c.R)/2), orientation=(0,0,1), length=c.L, radius=c.R, color=(1,0,0))
        self.O6 = sim.send_cylinder(position=(1.5*c.L,0,(c.L+c.R)/2), orientation=(0,0,1), length=c.L, radius=c.R, color=(0,1,0))
        self.O7 = sim.send_cylinder(position=(0,-1.5*c.L,(c.L+c.R)/2), orientation=(0,0,1), length=c.L, radius=c.R, color=(0,0,1))
        self.O8 = sim.send_cylinder(position=(-1.5*c.L,0,(c.L+c.R)/2), orientation=(0,0,1), length=c.L, radius=c.R, color=(1,0,1))

        self.O = {}
        self.O[0] = self.O0
        self.O[1] = self.O1
        self.O[2] = self.O2
        self.O[3] = self.O3
        self.O[4] = self.O4
        self.O[5] = self.O5
        self.O[6] = self.O6
        self.O[7] = self.O7
        self.O[8] = self.O8

    def send_joints(self,sim):
        # self.joint = sim.send_hinge_joint(self.whiteObject, self.redObject, (0, 0, 1.05), axis=(-1,0,0), joint_range=(3.14159/2))
        self.J0 = sim.send_hinge_joint(self.O0, self.O1, (0, c.L/2, c.L + c.R), axis=(-1,0,0))
        self.J1 = sim.send_hinge_joint(self.O0, self.O2, (c.L/2, 0, c.L+c.R), axis=(0,-1,0))
        self.J2 = sim.send_hinge_joint(self.O0, self.O3, (0, -c.L/2, c.L+c.R), axis=(-1,0,0))
        self.J3 = sim.send_hinge_joint(self.O0, self.O4, (-c.L/2, 0, c.L+c.R), axis=(0,-1,0))

        self.J4 = sim.send_hinge_joint(self.O1, self.O5, (0, 1.5*c.L, c.L + c.R), axis=(-1,0,0))
        self.J5 = sim.send_hinge_joint(self.O2, self.O6, (1.5*c.L, 0, c.L+c.R), axis=(0,-1,0))
        self.J6 = sim.send_hinge_joint(self.O3, self.O7, (0, -1.5*c.L, c.L+c.R), axis=(-1,0,0))
        self.J7 = sim.send_hinge_joint(self.O4, self.O8, (-1.5*c.L, 0, c.L+c.R), axis=(0,-1,0))

        self.J = {}
        self.J[0] = self.J0
        self.J[1] = self.J1
        self.J[2] = self.J2
        self.J[3] = self.J3
        self.J[4] = self.J4
        self.J[5] = self.J5
        self.J[6] = self.J6
        self.J[7] = self.J7
        
    
    def send_sensors(self,sim):
        self.T0 = sim.send_touch_sensor(body_id=self.O5)
        self.T1 = sim.send_touch_sensor(body_id=self.O6)
        self.T2 = sim.send_touch_sensor(body_id=self.O7)
        self.T3 = sim.send_touch_sensor(body_id=self.O8)
        self.P4 = sim.send_position_sensor(body_id=self.O0, which_dimension='x')
        self.P5 = sim.send_position_sensor(body_id=self.O0, which_dimension='y')
        self.P6 = sim.send_position_sensor(body_id=self.O0, which_dimension='z')

        self.S = {}
        self.S[0] = self.T0
        self.S[1] = self.T1
        self.S[2] = self.T2
        self.S[3] = self.T3


    def send_neurons(self,sim):
        self.SN = {}
        self.RA = {}
        self.MN = {}
        for s in self.S:
            self.SN[s] = sim.send_sensor_neuron(sensor_id=self.S[s])
        for j in self.J:
            self.RA[j] = sim.send_rotary_actuator(self.J[j])
            self.MN[j] = sim.send_motor_neuron(self.RA[j])


    def send_synapses(self,sim,wts):
        for j in self.SN:
            for i in self.MN:
                sim.send_synapse(source_neuron_id=self.SN[j], target_neuron_id=self.MN[i], weight=wts[j][i])