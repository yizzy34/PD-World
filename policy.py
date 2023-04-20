import random

class Policy:
    def __init__(self, agent, policy_type='PGREEDY'):
        self.agent = agent
        self.policy_type = policy_type

    def set_policy_type(self, policy_type):
        self.policy_type = policy_type

    def choose_action(self, state):
        if self.policy_type == 'PRANDOM':
            return random.choice(range(self.agent.n_actions))  # This line has been changed
        elif self.policy_type == 'PGREEDY':
            return self.epsilon_greedy_policy(state)
        elif self.policy_type == 'PEXPLOIT':
            return self.exploit_policy(state)

