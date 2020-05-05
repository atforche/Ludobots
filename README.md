# Ludobots
This repo contains my work as I work through the Evolutionary Robotics course found at r/ludobots (https://www.reddit.com/r/ludobots/)

# Table of Contents
*[Empty.py](#empty)

*[Objects.py](#objects)

*[Joints.py](#joints)

*[Sensors.py](#sensors)

*[Neurons.py](#neurons)

*[Synapses.py](#synapses)

*[Search.py](#search)

*[Robot.py](#robot)

## <a name="empty">Empty.py</a>
In this file, a default pyrosim simulation is created and visualized. This is primarily a test of the installation of the pryrosim package.

## <a name="objects">Objects.py</a>
This file is a basic test of the different objects and parameters that can be sent to the pyrosim simulation. Two cylinders are introduced to the simulated environment and manipulated using their input parameters.

## <a name="joints">Joints.py</a>
This file is a basic introduction to joints in the pyrosim simulation. Joints are created by connecting two objects in the simulation space via an anchor points. The axis of rotation of these joints can then be specified to determine in which ways the two objects are allowed to move relative to each other.

## <a name="sensors">Sensors.py</a>
  This file is a basic introduction to the different sensor modules in the pyrosim simulation. There are three main types of sensors explored, including the touch, propioception, and ray sensors. The touch sensor returns a 0 or 1 depending on whether the body is touching another body or not. The propioception sensor returns the degree of a particular joint as it goes throughout its motion. The ray sensor casts a ray out into the environment and either returns the max length of the ray or the distance to the nearest obstacle.

## <a name="neurons">Neurons.py</a>
  This file is a basic introduction to the different types of neurons and motors found in the pyrosim simulation. A sensor neuron has the ability to pull the sensor value from a specified sensor at each timestep. A motor neuron provides an output that is the result of an activiation function being applied to its input at every time step. Finally, there is a rotary actuator which will take in the input from the motor neuron and adjust the joint to the specified angle.

## <a name="synapses">Synapses.py</a>
This file introduces the ability to connect neurons together and produce responses in the robot due to its envinronment. Both of the touch sensors are attached to the motor neuron, which controls the rotary actuator on the single joint of the robot. Changing the weight of each synapse connection changes the overal behavior of the robot.

## <a name="search">Search.py</a>
This file serves at the driver program for search the solution space of all available robots to observe robots with interesting characteristics. Initially, robots are all created with an identical physical structure but different brain weights and connections.

## <a name="robot">Robot.py</a>
This file serves as the class defintion for the ROBOT class. This class contains all the information necessary for creating the robot with various characteristics that will operate in the simulation.
