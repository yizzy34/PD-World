import environment


class State:
    def __init__(self, world_environment):
        self.world_environment = world_environment
        self.representation = {'male_position': {}, 'female_position': {}, 'male_carrying': False,
                               'female_carrying': False, 'cell_blocks': {}}
        self.set_State_Environment()
        self.find_Agent_Positions()
        self.set_Cell_Blocks()

    def set_State_Environment(self):
        self.environment = self.world_environment.environment

    def find_Agent_Positions(self):
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    agent = self.environment[x][y][z]['occupied_by']
                    if agent in ['m', 'f']:
                        self.representation[f'{agent}_position']['coords'] = [x, y, z]
                        self.representation[f'{agent}_position']['cell_type'] = self.environment[x][y][z]['type']

    def Toggle_Carrying(self, agent):
        key = f'{agent}_carrying'
        self.representation[key] = not self.representation[key]

    def set_Cell_Blocks(self):
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    cell_type = self.environment[x][y][z]['type']
                    if cell_type in ['pickup', 'dropoff']:
                        self.representation['cell_blocks'][(x, y, z)] = self.environment[x][y][z]['block_count']

    def update_Environment_And_State(self, old_coords, action, agent, carrying, new_position):
        self.world_environment.move_agent(old_coords, action, agent, carrying)
        self.find_Agent_Positions()
        if (new_position == 'dropoff' and carrying) or (new_position == 'pickup' and not carrying):
            self.Toggle_Carrying(agent)
        self.set_Cell_Blocks()
        self.set_State_Environment()


def find_Possible_Cells(state, agent, actions):
    position_key = f'{agent}_position'
    possible_cells = environment.get_cell_types(state.environment, state.representation[position_key]['coords'],
                                                actions)
    return possible_cells


def find_Next_Position_Possible_Cells(state, coords, actions):
    possible_cells = environment.get_cell_types(state.environment, coords, actions)
    return possible_cells
