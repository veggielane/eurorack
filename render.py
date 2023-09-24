import os
#os.environ['PYOPENGL_PLATFORM'] = 'osmesa'
import trimesh
import pyrender
import numpy as np
from PIL import Image


def render_mesh(input, output):
    fuze_trimesh = trimesh.load(input)
    mesh = pyrender.Mesh.from_trimesh(fuze_trimesh)
    scene = pyrender.Scene()
    scene.add(mesh)

    camera = pyrender.OrthographicCamera(xmag=150.0, ymag=150.0, zfar=1000.0,znear=0.1)
    camera_pose = np.array([
    [1.0, 0.0, 0.0, 0],
    [0.0, 1.0, 0.0, 0],
    [0.0, 0.0, 1.0, 100],
    [0.0, 0.0, 0.0, 1.0],
    ])
    scene.add(camera, pose=camera_pose)

    r = pyrender.OffscreenRenderer(400, 400)
    color, depth = r.render(scene)
    img = Image.fromarray(color)
    img.save(output)