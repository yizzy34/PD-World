import reward
import value
import policy


class Qtable:
    def __init__(self):
        self.table = {
            'carrying': {
                'normal': {
                    'up': 0,
                    'down': 0,
                    'left': 0,
                    'right': 0,
                    'forward': 0,
                    'backward': 0
                },
                'risky': {
                    'up': 0,
                    'down': 0,
                    'left': 0,
                    'right': 0,
                    'forward': 0,
                    'backward': 0
                },
                'pickup': {
                    'up': 0,
                    'down': 0,
                    'left': 0,
                    'right': 0,
                    'forward': 0,
                    'backward': 0
                },
                'dropoff': {
                    'up': 0,
                    'down': 0,
                    'left': 0,
                    'right': 0,
                    'forward': 0,
                    'backward': 0
                }
            },
            'not_carrying': {
                'normal': {
                    'up': 0,
                    'down': 0,
                    'left': 0,
                    'right': 0,
                    'forward': 0,
                    'backward': 0
                },
                'risky': {
                    'up': 0,
                    'down': 0,
                    'left': 0,
                    'right': 0,
                    'forward': 0,
                    'backward': 0
                },
                'pickup': {
                    'up': 0,
                    'down': 0,
                    'left': 0,
                    'right': 0,
                    'forward': 0,
                    'backward': 0
                },
                'dropoff': {
                    'up': 0,
                    'down': 0,
                    'left': 0,
                    'right': 0,
                    'forward': 0,
                    'backward': 0
                }
            }
        }

    def choose_New_Q_Value(self, old_q_val, action_reward, next_q_vals, rl_method, chosen_policy, carrying,
                           next_pos_cells, alpha, gamma):
        if rl_method == 'q_learning':
            return round(value.q_Learning_Value_Function(old_q_val, action_reward, next_q_vals, alpha, gamma), 2)
        else:
            chosen_action = ''
            match chosen_policy:
                case 'p_random':
                    chosen_action = policy.p_Random(carrying, next_pos_cells)
                case 'p_exploit':
                    chosen_action = policy.p_Exploit(carrying, next_pos_cells, next_q_vals)
                case 'p_greedy':
                    chosen_action = policy.p_Greedy(carrying, next_pos_cells, next_q_vals)
            return round(value.sarsa_Value_Function(old_q_val, action_reward, next_q_vals[chosen_action], alpha, gamma),
                         2)

    def update_Q_Table(self, position, action, layer, next_cell, next_actions, alpha, gamma, rl_method='q_learning',
                       policy='p_random', carrying=False, next_pos_cells=None):
        old_q_val = self.table[layer][position][action]
        action_reward = reward.get_Reward(position)
        next_q_vals = self.find_Q_values(next_cell, next_actions, layer)
        new_q_val = self.choose_New_Q_Value(old_q_val, action_reward, next_q_vals, rl_method, policy, carrying,
                                            next_pos_cells, alpha, gamma)
        self.table[layer][position][action] = new_q_val

    def find_Q_values(self, position, actions, carrying):
        q_vals = {}
        for direction in actions:
            q_vals[direction] = self.table[carrying][position][direction]
        return q_vals
