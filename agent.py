import numpy as np
from policy import Policy
from value import ValueFunction


class QLearningAgent:
    def __init__(self, environment, state_representation, n_actions, alpha=0.3, gamma=0.5):
        self.environment = environment
        self.state_representation = state_representation
        self.n_actions = n_actions
        self.alpha = alpha
        self.gamma = gamma
        self.q_table = np.zeros((self.environment.get_n_states(), self.n_actions))
        self.value_function = ValueFunction(self.environment.get_n_states(), self.n_actions, alpha=self.alpha, gamma=self.gamma)
        self.policy = Policy(self, 'PGREEDY')

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
        self.value_function = ValueFunction(len(self.q_table), n_actions, alpha=self.alpha, gamma=self.gamma)

