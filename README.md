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

*[RandomSearch.py](#randomsearch)

*[Individual.py](#individual)

*[HillClimber.py](#hillclimber)

*[Playback.py](#playback)

*[Population.py](#population)

*[ParallelHillClimber](#parallel)

*[MinimalRobot.py](#minimal)

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
This file serves as the class defintion for the ROBOT class. This class contains all the information necessary for creating the robot with various characteristics that will operate in the simulation. The complexity of the neural network operating the robot was increased and modified for scalability of the neural network. The simple robot implement was moved to minimalRobot.py and this file now contains the quadrapedal robot.

## <a name="randomsearch">RandomSearch.py</a>
This file is the beginnings of a random search algorithm through the robot solution space. Robots are generated with a random synapse weight and the fitness is defined as the distance in the y direction that the robot moves. There currently is no form of selection implemented.

## <a name="individual">Individual.py</a>
This file contains the INDIVIDUAL class, which contains both a robot and a simulation. The robot is created and evalutated within the context of the simulation. The fitness of the individual is updated after the simulation is run, and this can be retrieved from the class. The mutation function for an individual is defined as a Gaussian curve centered around the current synapse weight with a standard deviation equal to the absolute value of the current weight. This promotes mutations that different from the current weight by a small amount, however larger mutations are still possible just with a lower probability. The Evaluate method was broken up into a Start_Evaluation and a Compute_Fitness method to enable multiple pyrosim simulations to be operated in parallel. Also, the mutations were modified to only modify a randomly selected synapse weight. Genome weights were modified to be a 2D array to reflect the fully connected layer between the touch sensors and the robots motor neurons.

## <a name="hillclimber">HillClimber.py</a>
This file introduces a new search strategy for exploring the robot solution landscape. This strategy focuses on smaller changes to the genotype to slowing climb the hill of the fitness landscape. Smaller mutations allow for the robots to exhibit more directional progress toward the goal. The best current robot is stored after each generation and every mutated robot is an offspring from the current best. This preserves a sense of forward progress in the population.

## <a name="playback">Playback.py</a>
This file gives the ability to play back brains that have been previously evolved using the Python Pickle library.

## <a name="population">Population.py</a>
This class groups together a population of individuals for evaluated and mutation. This allows for a group of individuals to be evaluated simultaenously, and selection can be performs on every individual at once.

## <a name="parallel">ParallelHillClimber.py</a>
This file introduces another new search strategy for exploring the robot solution landscape. As the complexity of the neural networks increase, the number of local optima in the fitness landscape increases. In order to combat this, multiple hill climbers are set at different points in the fitness space and evaluated in parallel. By having multiple hill climbers spread around the landscape, the odds of a single hill climber climbing all the way to the global maxmia increases.

## <a name="minimal">MinimalRobot.py</a>
This file contains a minimal Robot made up of two cylinders, a single joint, and a single motor neuron.
