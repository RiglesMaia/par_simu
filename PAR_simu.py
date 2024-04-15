#R.Maia
#PAR simulation

import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Constants
lat = -22.1838  # decimal degrees
jo = 118.11  # solar constant 118.11 MJ/m2.day or 1367 W/m2
#interval in julian days 
ND_i = 1     
ND_f = 365


#Calculate the Earth-Sun distance correction
def dD(day):
    distance = 1 + 0.033 * math.cos(math.radians(day * (360 / 365)))
    return distance

#Calculate solar declination
def g(day):
    declination = 23.45 * math.sin(math.radians(360 * (284 + day) / 365))
    return declination

#Calculate solar hour angle
def hn(declination):
    angle_hour = math.degrees(math.acos(-math.tan(math.radians(lat)) * math.tan(math.radians(declination))))
    return angle_hour

#Calculate extraterrestrial solar radiation
def q0(day):
    distance = dD(day)
    declination = g(day)
    angle_hour = hn(declination)
    rad_ex = (jo / math.pi) * distance * ((math.pi / 180) * angle_hour * math.sin(math.radians(lat)) * math.sin(math.radians(declination)) + math.cos(math.radians(lat)) * math.cos(math.radians(declination)) * math.sin(math.radians(angle_hour)))
    return rad_ex

#Calculate Photosynthetically Active Radiation (PAR)
def par(day, rad_ex):
    qg = 0.5 * rad_ex
    PAR = 0.5 * qg
    return PAR

# Lists to store calculated values
distances = []
declinations = []
angle_hours = []
rad_extras = []
pars = []

# Loop to calculate values
for i in range(ND_i, ND_f):
    distance = dD(i)
    declination = g(i)
    angle_hour = hn(declination)
    rad_ex = q0(i)
    PAR = par(i, rad_ex)
    distances.append(distance)
    declinations.append(declination)
    angle_hours.append(angle_hour)
    rad_extras.append(rad_ex)
    pars.append(PAR)
  
    print(f'Day {i} dD ~= {distance:.4f} UA // g ~= {declination:.4f} degrees // hn ~= {angle_hour:.4f} degrees // q0 ~= {rad_ex:.4f} MJ/m2.day // PAR ~= {PAR} MJ/m2.day') 

# Plotting the separate graphs
fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, 1, figsize=(8, 6))

# Plot 1: 
ax1.plot(declinations, color='orange')
ax1.set_ylabel('g (°)')
ax1.set_xlabel('Day of Year')
ax1.legend()

# Plot 2: 
ax2.plot(distances, color='purple')
ax2.set_ylabel('dD (AU)')
ax2.set_xlabel('Day of Year')
ax2.legend()

# Plot 3: 
ax3.plot(angle_hours, color='green')
ax3.set_ylabel('Hn (°)')
ax3.set_xlabel('Day of Year')
ax3.legend()

# Plot 4: 
ax4.plot(rad_extras, color='blue')
ax4.set_ylabel('Q0 (MJ/m².day)')
ax4.set_xlabel('Day of Year')
ax4.legend()

# Plot 5: 
ax5.plot(pars, color='red')
ax5.set_ylabel('PAR (MJ/m².day)')
ax5.set_xlabel('Day of Year')
ax5.legend()

plt.tight_layout()
plt.show()

