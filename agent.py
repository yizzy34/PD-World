import numpy as np
import random


class QLearningAgent:
    def __init__(self, environment, alpha=0.3, gamma=0.5, n_actions=8, epsilon=0.1):
        self.environment = environment
        self.alpha = alpha
        self.gamma = gamma
        self.n_actions = n_actions
        self.epsilon = epsilon
        self.q_table = {}

    def get_q(self, state, action):
        if (state, action) not in self.q_table:
            self.q_table[(state, action)] = 0
        return self.q_table[(state, action)]

    def update_q(self, state, action, value):
        self.q_table[(state, action)] = value

    def choose_action(self, state, policy):
        if policy == 'PRANDOM':
            return random.randint(0, self.n_actions - 1)
        elif policy == 'PGREEDY' or policy == 'PEXPLOIT':
            q_values = [self.get_q(state, a) for a in range(self.n_actions)]
            best_action = np.argmax(q_values)
            if policy == 'PGREEDY' or random.random() < self.epsilon:
                return best_action
            else:
                return random.randint(0, self.n_actions - 1)

    def learn(self, state, action, reward, next_state, next_action):
        q_value = self.get_q(state, action)
        next_q_value = self.get_q(next_state, next_action)
        value = q_value + self.alpha * (reward + self.gamma * next_q_value - q_value)
        self.update_q(state, action, value)
