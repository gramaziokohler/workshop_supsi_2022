from compas_fab.backends.kinematics.solvers import OffsetWristKinematics

from compas.geometry import Frame
from compas.robots import Configuration

f = Frame((0.417, 0.191, -0.005), (-0.000, 1.000, 0.00), (1.000, 0.000, 0.000))

UR10eKinematics = OffsetWristKinematics([0.1807, -0.6127, -0.57155, 0.17415, 0.11985, 0.11655])
solutions = UR10eKinematics.inverse(f)

for jv in solutions:
    print(Configuration.from_revolute_values(jv))
