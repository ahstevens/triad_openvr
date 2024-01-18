import triad_openvr
import matplotlib.pyplot as plt
import numpy as np

v = triad_openvr.triad_openvr("./config.json")

data = v.devices["vislab_tracker_1"].sample(1000,250)

#put xyz position data into 2d array for plotting
xyzs = np.vstack((data.x, data.y, data.z))

ax = plt.figure().add_subplot(projection='3d')

ax.plot(*xyzs, lw=1)
ax.set_xlabel("X Coordinate (meters)")
ax.set_ylabel("Y Coordinate (meters)")
ax.set_zlabel("Z Coordinate (meters)")
ax.set_title("Sampled Controller Coordinates")

plt.show()
