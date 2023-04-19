import random
import numpy as np
class Policy:
    def __init__(self, agent):
        self.agent = agent

    def choose_action(self, state, policy_type):
        if policy_type == 'PRANDOM':
            return self.random_policy(state)
        elif policy_type == 'PGREEDY':
            return self.epsilon_greedy_policy(state)
        elif policy_type == 'PEXPLOIT':
            return self.exploit_policy(state)
        else:
            raise ValueError(f"Invalid policy type: {policy_type}")

    def random_policy(self, state):
        return self.agent.get_random_action()

    def epsilon_greedy_policy(self, state):
        if random.random() < self.agent.epsilon:
            return self.agent.get_random_action()
        else:
            return self.agent.get_best_action(state)

    def exploit_policy(self, state):
        return self.agent.get_best_action(state)
