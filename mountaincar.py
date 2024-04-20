import gym
import numpy as np
import random
import time
import math
import matplotlib.pyplot as plt
from collections import deque



env = gym.make('MountainCar-v0', render_mode='rgb_array')

initial_state, info = env.reset(seed=42)

position = initial_state[0]
velocity = initial_state[1]

print(f"Initial position: {position}")
print(f"Initial velocity: {velocity}")

def render():
    state_image = env.render()
    plt.imshow(state_image)
    plt.show()
    
    
render()