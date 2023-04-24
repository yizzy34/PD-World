import action
import state
import policy


class Agent:
    def __init__(self, type, carrying=False):
        self.type = type
        self.carrying = carrying

    def toggle_carrying(self):
        # Toggle the carrying status of the agent
        self.carrying = not self.carrying


def set_possible_actions(state, agent):
    # Find the possible actions that an agent can take in a given state
    return action.find_possible_actions(state, agent)


def get_new_coords(state, agent, move):
    # Get the coordinates of the agent after it has moved in a given direction
    new_coords = []
    if agent == 'm':
        # Get the coordinates of the male agent
        old_coords = state.representation['male_position']['coords']
    else:
        # Get the coordinates of the female agent
        old_coords = state.representation['female_position']['coords']
    match move:
        case 'up':
            # Move the agent up
            new_coords = [old_coords[0] + 1, old_coords[1], old_coords[2]]
        case 'down':
            # Move the agent down
            new_coords = [old_coords[0] - 1, old_coords[1], old_coords[2]]
        case 'backward':
            # Move the agent backward
            new_coords = [old_coords[0], old_coords[1] + 1, old_coords[2]]
        case 'forward':
            # Move the agent forward
            new_coords = [old_coords[0], old_coords[1] - 1, old_coords[2]]
        case 'right':
            # Move the agent right
            new_coords = [old_coords[0], old_coords[1], old_coords[2] + 1]
        case 'left':
            # Move the agent left
            new_coords = [old_coords[0], old_coords[1], old_coords[2] - 1]
    return new_coords


def set_next_position_possible_actions(state, agent, move):
    # Find the possible actions that an agent can take from a given position
    new_coords = get_new_coords(state, agent, move)
    return action.find_next_position_possible_actions(new_coords)


def set_possible_cells(world_state, agent, actions):
    # Find the possible cells that an agent can move to in a given world state
    return state.find_possible_cells(world_state, agent, actions)


def set_next_position_possible_cells(world_state, coords, actions):
    # Find the possible cells that an agent can move to from a given position
    return state.find_next_position_possible_cells(world_state, coords, actions)


def set_possible_action_q_vals(state, agent, q_table, actions, layer):
    # Get the Q values for the possible actions in a given state and layer
    if agent == 'm':
        # Get the Q values for the male agent
        return q_table.find_q_vals(state.representation['male_position']['cell_type'], actions, layer)
    else:
        # Get the Q values for the female agent
        return q_table.find_q_vals(state.representation['female_position']['cell_type'], actions, layer)


def pickup_or_dropoff(agent, position):
    # Toggle the carrying status of the agent based on its current position
    if (position == 'pickup' and agent.carrying == False) or (position == 'dropoff' and agent.carrying == True):
        agent.toggle_carrying()


def choose_action(agent, cells, q_vals, chosen_policy='p_random'):
    # Choose an action based on the selected policy
    match chosen_policy:
        case 'p_random':
            return policy.p_random(agent.carrying, cells)
        case 'p_exploit':
            return policy.p_exploit(agent.carrying, cells, q_vals)
        case 'p_greedy':
            return policy.p_greedy(agent.carrying, cells, q_vals)


def determine_future_carrying(agent, cells, action):
    # Determine whether the agent should pick up or drop off an item, based on their current carrying status and position
    if (cells[action]['type'] == 'pickup' and cells[action]['is_empty'] == False and agent.carrying == False) or (
            cells[action]['type'] != 'dropoff' and agent.carrying):
        return True
    return False
