# Before running this example, make sure to run
# "docker compose up" on the docker folder
from compas.artists import Artist
from compas_fab.backends import RosClient

# Load robot and its geometry
with RosClient("localhost") as ros:
    robot = ros.load_robot(load_geometry=True, precision="12f")
    # robot already contains model, semantics and client
    robot.info()

    artist = Artist(robot.model)
    artist.draw_visual()
    artist.redraw()
