# N-Body-Simulation

Week 4 assignment from Intro to Python at JHU

Skills: lists, math/string functions, control structures (while loops), math operators

This assignment required me to simulate the motion of celestial bodies on a 2-D plane. My code models the gravitational forces between the sun and another planet within our solar system using classical kinematic equations. Python lists are used to store data for multiple planets and compute calculations at each step within the simulation.

For the purpose of this assignment, the input was hardcoded into my program. The input consists of a variable "t" that stores the total simulation time and "dt" which serves as a time step that the simulation will iterate through until the total time has elapsed. Five lists are also created for the five celestial bodies being simulated: Earth, Mars, Mercury, the Sun, and Venus. Each list contains the starting x and y coordinates, the x and y velocities, and the mass of each respective celestial body.

The program starts by calculating the total force between the sun and each of the planets. Next, it determines the x and y components of the total force, then determines the acceleration of each planet in the x and y direction. After, it calculates the velocity of the planet in the x and y direction and uses the velocity values to determine new x and y positions, which are updated in a list.  The program iterates through these steps until the total time has elapsed at which point the final output is printed.
