from environment import CustomEnvironment
import numpy as np
from value import ValueFunction


class QLearningAgent:
    def __init__(self, environment, n_actions, alpha=0.1, gamma=0.99, epsilon=0.1):
        self.environment = environment
        self.n_actions = n_actions
        self.epsilon = epsilon

        n_states = environment.get_n_states()
        self.value_function = ValueFunction(n_states, n_actions, alpha, gamma)

    def choose_action(self, state, policy):
        return policy.choose_action(self, state)

    def update(self, current_state, action, reward, next_state):
        self.value_function.update(current_state, action, reward, next_state)

    def get_q_value(self, state, action):
        return self.value_function.get_q_value(state, action)
