from gym import spaces
import numpy as np
import random
import gym
import time
import math
import matplotlib.pyplot as plt
from collections import deque

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import os
import copy
import sys

exp_rewards_strategy_1 = np.array([3, 2, -1, 5])

discount_factor = 0.9

# Compute discounts
discounts_strategy_1 = np.array([discount_factor ** i for i in range(len(exp_rewards_strategy_1))])

# Compute the discounted return
discounted_return_strategy_1 = np.sum(discounts_strategy_1 * discount_factor)

print(f"The discounted return of the first strategy is {discounted_return_strategy_1}")

exp_rewards_strategy_2 = np.array([6, -5, -3, -2])

discount_factor = 0.9

# Compute discounts
discounts_strategy_2 = np.array([discount_factor ** i for i in range(len(exp_rewards_strategy_2))])

# Compute the discounted return
discounted_return_strategy_2 = np.sum(discounts_strategy_2 * exp_rewards_strategy_2)

print(f"The discounted return of the second strategy is {discounted_return_strategy_2}")