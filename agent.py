import action
import state
import policy


# Define the Agent class
class Agent:
    def __init__(self, type, carrying=False):
        self.type = type
        self.carrying = carrying

    # Toggle the carrying status of the agent
    def toggle_carrying(self):
        self.carrying = not self.carrying


# Set the possible actions for an agent in a given state
def set_possible_actions(state, agent):
    return action.find_possible_actions(state, agent)


# Get the new coordinates for an agent in a given state after taking a given move
def get_new_coords(state, agent, move):
    new_coords = []
    # If the agent is male, get his current coordinates from the state dictionary
    if agent == 'm':
        old_coords = state.representation['male_position']['coords']
    # If the agent is female, get her current coordinates from the state dictionary
    else:
        old_coords = state.representation['female_position']['coords']
    # Determine the new coordinates based on the chosen move
    match move:
        case 'up':
            new_coords = [old_coords[0] + 1, old_coords[1], old_coords[2]]
        case 'down':
            new_coords = [old_coords[0] - 1, old_coords[1], old_coords[2]]
        case 'backward':
            new_coords = [old_coords[0], old_coords[1] + 1, old_coords[2]]
        case 'forward':
            new_coords = [old_coords[0], old_coords[1] - 1, old_coords[2]]
        case 'right':
            new_coords = [old_coords[0], old_coords[1], old_coords[2] + 1]
        case 'left':
            new_coords = [old_coords[0], old_coords[1], old_coords[2] - 1]
    # Return the new coordinates
    return new_coords


# Set the possible actions for an agent in the next position after taking a given move
def set_next_position_possible_actions(state, agent, move):
    # Get the new coordinates for the agent after taking the given move
    new_coords = get_new_coords(state, agent, move)
    # Return the possible actions for the agent in the next position
    return action.find_next_position_possible_actions(new_coords)


# Set the possible cells for an agent in a given world state, given their possible actions
def set_possible_cells(world_state, agent, actions):
    return state.find_possible_cells(world_state, agent, actions)


# Set the possible cells for an agent in the next position, given their current coordinates and possible actions
def set_next_position_possible_cells(world_state, coords, actions):
    return state.find_next_position_possible_cells(world_state, coords, actions)


# Set the Q-values for possible actions for a given agent in a given state
def set_possible_action_q_vals(state, agent, q_table, actions, layer):
    if agent == 'm':
        # If the agent is male, get the Q-values from the Q-table for his current cell type and possible actions
        return q_table.find_q_vals(state.representation['male_position']['cell_type'], actions, layer)
    else:
        # If the agent is female, get the Q-values from the Q-table for her current cell type and possible actions
        return q_table.find_q_vals(state.representation['female_position']['cell_type'], actions, layer)


# Determine whether the agent should pick up or drop off an item, based on their current carrying status and position
def pickup_or_dropoff(agent, position):
    # If the position is 'pickup' and the agent is not already carrying an item, or if the position is 'dropoff' and the agent is carrying an item
    if (position == 'pickup' and agent.carrying == False) or (position == 'dropoff' and agent.carrying == True):
        # Toggle the carrying status of the agent
        agent.toggle_carrying()


# Choose an action for the agent based on the chosen policy
def choose_action(agent, cells, q_vals, chosen_policy='p_random'):
    # Use a match statement to determine which policy to use
    match chosen_policy:
        case 'p_random':
            # If the chosen policy is 'p_random', choose an action randomly
            return policy.p_Random(agent.carrying, cells)
        case 'p_exploit':
            # If the chosen policy is 'p_exploit', choose the action with the highest Q-value
            return policy.p_Exploit(agent.carrying, cells, q_vals)
        case 'p_greedy':
            # If the chosen policy is 'p_greedy', choose the action with the highest Q-value with some probability of exploration
            return policy.p_Greedy(agent.carrying, cells, q_vals)


# Determine whether the agent should be carrying an item after taking a given action
def determine_future_carrying(agent, cells, action):
    # If the action is a pickup action and the agent is not already carrying an item, or if the action is not a dropoff action and the agent is carrying an item
    if (cells[action]['type'] == 'pickup' and cells[action]['is_empty'] == False and agent.carrying == False) or (
            cells[action]['type'] != 'dropoff' and agent.carrying):
        # The agent will be carrying an item in the future
        return True
    # Otherwise, the agent will not be carrying an item in the future
    return False
