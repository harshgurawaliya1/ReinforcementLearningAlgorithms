import gym 
import numpy as np
import random
import time
import math
import matplotlib.pyplot as plt


env = gym.make('FrozenLake-v1', render_mode='rgb_array')

initial_state, info = env.reset(seed=42)

actions = [1 , 1 , 2 , 2 , 1, 2]

def render():
    state_image = env.render()
    plt.imshow(state_image)
    plt.show()
    
for action in actions:
    state, reward, terminated, _, _ = env.step(action)
    render()
    if terminated:
        print("you have reached the goal")