import numpy as np


class ValueFunction:
    def __init__(self, n_states, n_actions, alpha=0.1, gamma=0.99):
        self.q_table = np.zeros((n_states, n_actions))
        self.alpha = alpha
        self.gamma = gamma

    def update(self, state, action, reward, next_state):
        current_q = self.q_table[state][action]
        max_next_q = np.max(self.q_table[next_state])
        new_q = current_q + self.alpha * (reward + self.gamma * max_next_q - current_q)
        self.q_table[state][action] = new_q

    def get_best_action(self, state):
        return np.argmax(self.q_table[state])

    def get_q_value(self, state, action):
        return self.q_table[state][action]
