# Ludobots
This repo contains my work as I work through the Evolutionary Robotics course found at r/ludobots (https://www.reddit.com/r/ludobots/)

# Table of Contents
*[Empty.py](#empty)

*[Objects.py](#objects)

*[Joints.py](#joints)

*[Sensors.py](#sensors)

## <a name="empty">Empty.py</a>
In this file, a default pyrosim simulation is created and visualized. This is primarily a test of the installation of the pryrosim package.

## <a name="objects">Objects.py</a>
This file is a basic test of the different objects and parameters that can be sent to the pyrosim simulation. Two cylinders are introduced to the simulated environment and manipulated using their input parameters.

## <a name="joints">Joints.py</a>
This file is a basic introduction to joints in the pyrosim simulation. Joints are created by connecting two objects in the simulation space via an anchor points. The axis of rotation of these joints can then be specified to determine in which ways the two objects are allowed to move relative to each other.

## <a name=sensors">Sensors.py</a>
  This file is a basic introduction to the different sensor modules in the pyrosim simulation. There are three main types of sensors explored, including the touch, propioception, and ray sensors. The touch sensor returns a 0 or 1 depending on whether the body is touching another body or not. The propioception sensor returns the degree of a particular joint as it goes throughout its motion. The ray sensor casts a ray out into the environment and either returns the max length of the ray or the distance to the nearest obstacle.
