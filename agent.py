from environment import CustomEnvironment
import numpy as np
from value import ValueFunction


class QLearningAgent:
    def __init__(self, environment, state_representation, n_actions, alpha=0.1, gamma=0.99):
        self.environment = environment
        self.state_representation = state_representation  # Add this line
        self.n_actions = n_actions
        self.alpha = alpha
        self.gamma = gamma
        self.q_table = np.zeros((self.environment.get_n_states(), n_actions))

    def choose_action(self, state, policy):
        return policy.choose_action(self, state)

    def update(self, current_state, action, reward, next_state):
        # Convert states to indices
        current_state_index = self.state_representation.state_to_index(current_state, self.environment.grid_size_x,
                                                                       self.environment.grid_size_y,
                                                                       self.environment.grid_size_z)
        next_state_index = self.state_representation.state_to_index(next_state, self.environment.grid_size_x,
                                                                    self.environment.grid_size_y,
                                                                    self.environment.grid_size_z)

        self.value_function.update(current_state_index, action, reward, next_state_index)

    def get_q_value(self, state, action):
        return self.value_function.get_q_value(state, action)
