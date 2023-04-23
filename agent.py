import action
import state
import policy


class Agent:
    def __init__(self, agent_type, carrying=False):
        self.agent_type = agent_type
        self.carrying = carrying

    def toggle_Carrying(self):
        self.carrying = not self.carrying


def set_Possible_Actions(state, agent_type):
    return action.find_Possible_Actions(state, agent_type)


def get_New_Coordinates(state, agent_type, move):
    new_coordinates = []
    if agent_type == 'm':
        old_coordinates = state.representation['male_position']['coords']
    else:
        old_coordinates = state.representation['female_position']['coords']
    match move:
        case 'up':
            new_coordinates = [old_coordinates[0] + 1, old_coordinates[1], old_coordinates[2]]
        case 'down':
            new_coordinates = [old_coordinates[0] - 1, old_coordinates[1], old_coordinates[2]]
        case 'backward':
            new_coordinates = [old_coordinates[0], old_coordinates[1] + 1, old_coordinates[2]]
        case 'forward':
            new_coordinates = [old_coordinates[0], old_coordinates[1] - 1, old_coordinates[2]]
        case 'right':
            new_coordinates = [old_coordinates[0], old_coordinates[1], old_coordinates[2] + 1]
        case 'left':
            new_coordinates = [old_coordinates[0], old_coordinates[1], old_coordinates[2] - 1]
    return new_coordinates


def set_Next_Position_Possible_Actions(state, agent_type, move):
    new_coordinates = get_New_Coordinates(state, agent_type, move)
    return action.find_Next_Position_Possible_Actions(new_coordinates)


def set_Possible_Cells(world_state, agent_type, actions):
    return state.find_Possible_Cells(world_state, agent_type, actions)


def set_Next_Position_Possible_Cells(world_state, coordinates, actions):
    return state.find_Next_Position_Possible_Cells(world_state, coordinates, actions)


def set_Possible_Action_Q_values(state, agent_type, q_table, actions, layer):
    if agent_type == 'm':
        return q_table.find_q_vals(state.representation['male_position']['cell_type'], actions, layer)
    else:
        return q_table.find_q_vals(state.representation['female_position']['cell_type'], actions, layer)


def pickup_Or_Dropoff(agent, position):
    if (position == 'pickup' and agent.carrying == False) or (position == 'dropoff' and agent.carrying == True):
        agent.toggle_Carrying()


def choose_Action(agent, cells, q_vals, chosen_policy='p_random'):
    match chosen_policy:
        case 'p_random':
            return policy.p_Random(agent.carrying, cells)
        case 'p_exploit':
            return policy.p_Exploit(agent.carrying, cells, q_vals)
        case 'p_greedy':
            return policy.p_Greedy(agent.carrying, cells, q_vals)


def determine_Future_Carrying(agent, cells, action):
    if (cells[action]['type'] == 'pickup' and cells[action]['is_empty'] == False and agent.carrying == False) or (
            cells[action]['type'] != 'dropoff' and agent.carrying):
        return True
    return False
