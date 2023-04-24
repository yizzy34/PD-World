import reward
import value
import policy


class Qtable:
    def __init__(self):
        # initialize the Q-table with 0 values for all state-action pairs
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

    def choose_new_q_val(self, old_q_val, action_reward, next_q_vals, rl_method, chosen_policy, carrying,
                           next_pos_cells, alpha, gamma):
        # select a new Q-value based on the RL method and policy used
        if rl_method == 'q_learning':
            # use the Q-learning update rule
            return round(value.q_Learning_Value_Function(old_q_val, action_reward, next_q_vals, alpha, gamma), 2)
        else:
            # use the SARSA update rule, and choose the next action based on the chosen policy
            chosen_action = ''
            match chosen_policy:
                case 'p_random':
                    chosen_action = policy.p_Random(carrying, next_pos_cells)
                case 'p_exploit':
                    chosen_action = policy.p_Exploit(carrying, next_pos_cells, next_q_vals)
                case 'p_greedy':
                    chosen_action = policy.p_Greedy(carrying, next_pos_cells, next_q_vals)
            return round(value.sarsa_Value_Function(old_q_val, action_reward, next_q_vals[chosen_action], alpha, gamma),2)

    def update_qtable(self, position, action, layer, next_cell, next_actions, alpha, gamma, rl_method='q_learning',
                       policy='p_random', carrying=False, next_pos_cells=None):
        """
        Update the Q-table for the given state-action pair using the chosen RL algorithm and policy.

        Args:
        - position (str): The current position of the agent.
        - action (str): The current action taken by the agent.
        - layer (str): The current layer of the environment (carrying/not_carrying).
        - next_cell (str): The next cell that the agent will move to.
        - next_actions (list of str): The possible actions that the agent can take from the next cell.
        - alpha (float): The learning rate.
        - gamma (float): The discount factor.
        - rl_method (str, optional): The chosen RL algorithm to use (q_learning/sarsa). Defaults to 'q_learning'.
        - policy (str, optional): The chosen policy to use for updating the Q-values (p_random/p_exploit/p_greedy). Defaults to 'p_random'.
        - carrying (bool, optional): Whether the agent is carrying a package or not. Defaults to False.
        - next_pos_cells (list of str, optional): The possible cells that the agent can move to from the next cell. Only used for the p_random policy. Defaults to None.
        """
        # Get the old Q-value for the current state-action pair
        old_q_val = self.table[layer][position][action]

        # Get the reward for the current state
        action_reward = reward.get_Reward(position)

        # Get the Q-values for the possible next actions from the next cell
        next_q_vals = self.find_Q_values(next_cell, next_actions, layer)

        # Choose the new Q-value based on the chosen RL algorithm and policy
        new_q_val = self.choose_New_Q_Value(old_q_val, action_reward, next_q_vals, rl_method, policy, carrying,
                                            next_pos_cells, alpha, gamma)

        # Update the Q-table with the new Q-value for the current state-action pair
        self.table[layer][position][action] = new_q_val

    def find_q_vals(self, position, actions, carrying):
        """
        Get the Q-values for the given state and possible actions.

        Args:
        - position (str): The current position of the agent.
        - actions (list of str): The possible actions that the agent can take from the current position.
        - carrying (bool): Whether the agent is carrying a package or not.

        Returns:
        - q_vals (dict): A dictionary mapping each action to its corresponding Q-value for the given state.
        """
        # Initialize an empty dictionary for the Q-values
        q_vals = {}

        # Get the Q-value for each possible action from the Q-table
        for direction in actions:
            q_vals[direction] = self.table[carrying][position][direction]

        # Return the dictionary of Q-values
        return q_vals

