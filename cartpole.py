import gym  
import numpy as np
import random
import time
import math
import matplotlib.pyplot as plt
from collections import deque
import torch

env = gym.make('CartPole-v1', render_mode='rgb_array')
state, info = env.reset(seed= 42) 
print(state)

def render():
    state_image = env.render()
    plt.imshow(state_image)
    plt.show()
    
render()

terminated = False
while not terminated:
    action = 1  #move to right

    state, reward, terminated, _, _ = env.step(action)
    render()

print(f"State: {state}")
print(f"Reward: {reward}")
print(f"Terminated: {terminated}")