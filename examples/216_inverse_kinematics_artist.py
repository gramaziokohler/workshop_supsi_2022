import os

from compas_fab.backends.kinematics.solvers import OffsetWristKinematics

from compas.artists import Artist
from compas.geometry import Frame
from compas.robots import LocalPackageMeshLoader
from compas.robots import RobotModel

DATA = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
model = RobotModel.from_urdf_file(os.path.join(DATA, 'ur10e.urdf'))
loader = LocalPackageMeshLoader(DATA, 'ur_description')
model.load_geometry(loader)

f = Frame((0.417, 0.191, -0.005), (-0.000, 1.000, 0.000), (1.000, 0.000, 0.00))

UR10eKinematics = OffsetWristKinematics([0.1807, -0.6127, -0.57155, 0.17415, 0.11985, 0.11655])
solutions = UR10eKinematics.inverse(f)

artist = Artist(model, layer='IK')

for jv in solutions:
    config = model.zero_configuration()
    config.joint_values = jv
    artist.update(config)
    artist.draw()
    artist.redraw(1)
    artist.clear_layer()
