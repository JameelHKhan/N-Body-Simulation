# Module 4 Assignment
# Jameel H. Khan

# importing "math" for mathematical operations
import math

# lists for input data: position x-y, velocity x-y, mass
px = [1.4960e+11, 2.2790e+11, 5.7900e+10, 0.0000e+00, 1.0820e+11]
py = [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00]
vx = [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00]
vy = [2.9800e+04, 2.4100e+04, 4.7900e+04, 0.0000e+00, 3.5000e+04]
m = [5.9740e+24, 6.4190e+23, 3.3020e+23, 1.9890e+30, 4.8690e+24]

# lists for calculations
rSqr = [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00]
r = [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00]
f = [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00]
fx = [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00]
fy = [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00]
ax = [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00]
ay = [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00]

t_total = 0.0           # control for while loop
dt = 25000.0            # time step
t = 157788000           # time length
N = 5                   # iterations for for loop
G = 6.67e-11            # gravitational constant
SUN = 3                 # index value of data for sun within lists

while t_total < t:
    for i in range(N):
        if i == SUN:    # skip calculations for the sun
            continue
        else:
            # calculate radius squared between planet and sun
            rSqr[i] = (px[i]**2) + (py[i]**2)
            # take the square root of rSqr to get the actual radius
            r[i] = math.sqrt(rSqr[i])
            # calculate pair-wise force between two bodies
            # originally, I did not have the negative sign in this calculation
            # however my output always came out incorrect. My professor 
            # suggested that I negate my Force value, which correct my output.
            f[i] = -((G * m[i] * m[3])/rSqr[i])
            # calculate x component of total force
            fx[i] = (px[i]/r[i]) * f[i]
            # calculate y component of total force
            fy[i] = (py[i]/r[i]) * f[i]
            # calculate x component of acceleration
            ax[i] = fx[i]/m[i]
            # calculate y component of acceleration
            ay[i] = fy[i]/m[i]
            # calculate x component of new velocity
            vx[i] = (ax[i] * dt) + vx[i]
            # calculate y component of new velocity
            vy[i] = (ay[i] * dt) + vy[i]
            # calculate and assign new x component of position
            px[i] = (vx[i] * dt) + px[i]
            # calculate and assign new y component of position
            py[i] = (vy[i] * dt) + py[i]
            # end of if statement
        # end of for loop
    t_total += dt
    # end of while loop

for i in range(N): # print loop for formatted output in scientific notation
                   # and to four decimal places
    print(f"{px[i]:.4e} {py[i]:.4e} {vx[i]:.4e} {vy[i]:.4e} {m[i]:.4e}")
