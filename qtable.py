import reward
import value
import policy


class Qtable:
    def __init__(self):
        self.table = {
            'carrying': {
                'normal': {
                    'up': 5,
                    'down': 12,
                    'left': 3,
                    'right': 8,
                    'forward': 4,
                    'backward': 7
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
                    'up': 5,
                    'down': 12,
                    'left': 3,
                    'right': 8,
                    'forward': 4,
                    'backward': 7
                }
            },
            'not_carrying': {
                'normal': {
                    'up': 5,
                    'down': 12,
                    'left': 3,
                    'right': 8,
                    'forward': 4,
                    'backward': 7
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
                    'up': 5,
                    'down': 12,
                    'left': 3,
                    'right': 8,
                    'forward': 4,
                    'backward': 7
                }
            }
        }

    def choose_New_Q_Value(self, old_q_val, move_reward, next_q_vals, rl_method, chosen_policy, carrying,
                           next_pos_cells,
                           alpha, gamma):
        print('rl_method ', rl_method)
        if rl_method == 'q_learning':
            return round(value.q_learning_value_function(old_q_val, move_reward, next_q_vals, alpha, gamma), 2)
        else:
            chosen_action = ''
            match chosen_policy:
                case 'p_random':
                    chosen_action = policy.p_random(carrying, next_pos_cells)
                case 'p_exploit':
                    chosen_action = policy.p_exploit(carrying, next_pos_cells, next_q_vals)
                case 'p_greedy':
                    chosen_action = policy.p_greedy(carrying, next_pos_cells, next_q_vals)
            return round(value.sarsa_value_function(old_q_val, move_reward, next_q_vals[chosen_action], alpha, gamma),
                         2)

    def update_Qtable(self, position, move, layer, next_cell, next_actions, alpha, gamma, rl_method='q_learning',
                      policy='p_random', carrying=False, next_pos_cells=None):
        old_q_val = self.table[layer][position][move]
        move_reward = reward.get_reward(position)
        next_q_vals = self.find_Q_Values(next_cell, next_actions, layer)
        new_q_val = self.choose_New_Q_Value(old_q_val, move_reward, next_q_vals, rl_method, policy, carrying,
                                            next_pos_cells, alpha, gamma)
        print('new_q_val ', new_q_val)
        self.table[layer][position][move] = new_q_val
        print('new_q_val in q_table ', self.table[layer][position][move])

    def find_Q_Values(self, position, moves, carrying):
        print("position ", position)
        q_vals = {}
        for direction in moves:
            q_vals[direction] = self.table[carrying][position][direction]
        return q_vals
