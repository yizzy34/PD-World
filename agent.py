import action
import state
import policy


class Agent:
    def __init__(self, type, carrying=False):
        self.type = type
        self.carrying = carrying

    def toggle_carrying(self):
        self.carrying = not self.carrying


def set_possible_actions(state, agent):
    return action.find_possible_actions(state, agent)


def get_new_coords(state, agent, move):
    new_coords = []
    if agent == 'm':
        old_coords = state.representation['male_position']['coords']
    else:
        old_coords = state.representation['female_position']['coords']
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
    return new_coords


def set_next_position_possible_actions(state, agent, move):
    new_coords = get_new_coords(state, agent, move)
    return action.find_next_position_possible_actions(new_coords)


def set_possible_cells(world_state, agent, actions):
    return state.find_possible_cells(world_state, agent, actions)


def set_next_position_possible_cells(world_state, coords, actions):
    return state.find_next_position_possible_cells(world_state, coords, actions)


def set_possible_action_q_vals(state, agent, q_table, actions, layer):
    if agent == 'm':
        return q_table.find_q_vals(state.representation['male_position']['cell_type'], actions, layer)
    else:
        return q_table.find_q_vals(state.representation['female_position']['cell_type'], actions, layer)


def pickup_or_dropoff(agent, position):
    if (position == 'pickup' and agent.carrying == False) or (position == 'dropoff' and agent.carrying == True):
        agent.toggle_carrying()


def choose_action(agent, cells, q_vals, chosen_policy='p_random'):
    match chosen_policy:
        case 'p_random':
            return policy.p_random(agent.carrying, cells)
        case 'p_exploit':
            return policy.p_exploit(agent.carrying, cells, q_vals)
        case 'p_greedy':
            return policy.p_greedy(agent.carrying, cells, q_vals)


def determine_future_carrying(agent, cells, action):
    if (cells[action]['type'] == 'pickup' and cells[action]['is_empty'] == False and agent.carrying == False) or (
            cells[action]['type'] != 'dropoff' and agent.carrying):
        return True
    return False
