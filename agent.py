import action
import qtable
import state
import environment
import policy


class Agent:
    def __init__(self, agent_type, carrying=False):
        self.agent_type = agent_type
        self.carrying = carrying

    def toggle_Carrying(self):
        self.carrying = not self.carrying


def set_Possible_Actions(state, agent_type):
    return action.find_possible_actions(state, agent_type)


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
    return action.find_next_position_possible_actions(new_coordinates)


def set_Possible_Cells(world_state, agent_type, actions):
    return state.find_possible_cells(world_state, agent_type, actions)


def set_Next_Position_Possible_Cells(world_state, coordinates, actions):
    return state.find_next_position_possible_cells(world_state, coordinates, actions)


def set_Possible_Action_Qvalues(state, agent_type, q_table, actions, layer):
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
            return policy.p_random(agent.carrying, cells)
        case 'p_exploit':
            return policy.p_exploit(agent.carrying, cells, q_vals)
        case 'p_greedy':
            return policy.p_greedy(agent.carrying, cells, q_vals)


def determine_Future_Carrying(agent, cells, action):
    if (cells[action]['type'] == 'pickup' and cells[action]['is_empty'] == False and agent.carrying == False) or (
            cells[action]['type'] != 'dropoff' and agent.carrying):
        return True
    return False


def main():
    rl_method = 'sarsa'
    chosen_policy = 'p_greedy'
    env = environment.Environment()
    # Initialize state with environment object
    world_state = state.State(env)
    q_table = qtable.Qtable()
    agent = Agent('m')
    for i in range(10):
        print('\nMOVE ', i)
        layer = ''
        match agent.carrying:
            case True:
                layer = 'carrying'
            case False:
                layer = 'not_carrying'
        actions = set_Possible_Actions(world_state, agent.agent_type)
        print('actions ', actions)
        cells = set_Possible_Cells(world_state, agent.agent_type, actions)
        print('cells ', cells)
        q_vals = set_Possible_Action_Qvalues(world_state, agent.agent_type, q_table, actions, layer)
        print('q_vals ', q_vals)
        chosen_action = choose_Action(agent, cells, q_vals, chosen_policy)
        print('chosen_action ', chosen_action)
        next_pos_actions = set_Next_Position_Possible_Actions(world_state, agent.agent_type, chosen_action)
        print('next_pos_actions ', next_pos_actions)
        next_pos_cells = set_Next_Position_Possible_Cells(world_state, cells[chosen_action]['coords'], next_pos_actions)
        print('next_pos_cells ', next_pos_cells)
        future_carrying = False
        if (rl_method == 'sarsa'):
            future_carrying = determine_Future_Carrying(agent, cells, chosen_action)
        q_table.update_qtable(world_state.representation['male_position']['cell_type'], chosen_action, layer,
                              cells[chosen_action]['type'], next_pos_actions, 0.2, 0.6, rl_method, chosen_policy,
                              future_carrying, next_pos_cells)
        print(q_table.table)
        print('agent carrying', agent.carrying)
        if agent.agent_type == 'm':
            world_state.update_environment_and_state(world_state.representation['male_position']['coords'],
                                                     chosen_action, agent.agent_type, agent.carrying,
                                                     cells[chosen_action]['type'])
        else:
            world_state.update_environment_and_state(world_state.representation['female_position']['coords'],
                                                     chosen_action, agent.agent_type, agent.carrying,
                                                     cells[chosen_action]['type'])
        if cells[chosen_action]['type'] == 'pickup' or cells[chosen_action]['type'] == 'dropoff':
            pickup_Or_Dropoff(agent, cells[chosen_action]['type'])
        print('new environment:')
        for x in range(3):
            print(f'\nLevel {x}\n')
            for y in range(3):
                print(f'\nRow {y}\n')
                for z in range(3):
                    print(world_state.environment[x][y][z])
