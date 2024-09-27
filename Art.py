import bpy # Importing Blender-Python Functionality
import math # importing math 
import random # randomness

# setup the basic variables to store our primitive mesh information
verts = []
edges = []
faces = []

# Set a vertex randomly along the y direction from a range of 1 -> 5
verts.append([0, random.uniform(1,5), 0])

# Set two mirrored vertices for a clean triangle from the range -5 -> 5
verts.append([random.uniform(0,-5), 0, 0])
verts.append([random.uniform(0,5), 0, 0])

# Basic circular array methods used to join the edges
for i in range(3):
    edges.append([i, ((i + 1) % 3)])

mesh_data = bpy.data.meshes.new("Triangle data")
mesh_data.from_pydata(verts, edges, faces)

mesh_obj = bpy.data.objects.new("Triangle Object", mesh_data)

bpy.context.collection.objects.link(mesh_obj)