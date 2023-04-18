import random
import numpy as np

def choose_action(agent, state, policy):
    if policy == 'PRANDOM':
        return random.randint(0, agent.n_actions - 1)
    elif policy == 'PGREEDY' or policy == 'PEXPLOIT':
        q_values = [agent.get_q(state, a) for a in range(agent.n_actions)]
        best_action = np.argmax(q_values)
        if policy == 'PGREEDY' or random.random() < agent.epsilon:
            return best_action
        else:
            return random.randint(0, agent.n_actions - 1)
