swarm = []
import numpy as np

with open("inputs/particle_swarm.txt") as file:
    for line in file:
        pos, vel, acc = line[:-1].split()
        pos = pos[:-1]
        vel = vel[:-1]
        exec(pos), exec(vel), exec(acc)
        swarm.append([np.array(p,dtype=int), np.array(v,dtype=int), np.array(a,dtype=int)])

def update(swarm):

    point_cloud = set({})
    collision_set = set({})
    num_points = 0

    for label, particle in enumerate(swarm):
        particle[1] += particle[2] # Note order of update!
        particle[0] += particle[1]
        point_cloud.add(tuple(particle[0]))
        if len(point_cloud) == num_points:
            print("collision!")
            collision_set.add(tuple(particle[0]))
        num_points = len(point_cloud)

    return [particle for particle in swarm if tuple(particle[0]) not in collision_set]

def closest(swarm):
    return np.argmin([sum(abs(particle[0])) for particle in swarm])

for _ in range(1000):
    print(len(swarm))
    swarm = update(swarm)
