import environment


class State:
    def __init__(self, world_environment):
        self.world_environment = world_environment
        self.representation = {'male_position': {}, 'female_position': {}, 'male_carrying': False,
                               'female_carrying': False, 'pickup_cell_blocks': {}, 'dropoff_cell_blocks': {}}
        self.set_State_Environment()
        self.set_Male_Position()
        self.set_Female_Position()
        self.set_Pickup_Cell_Blocks()
        self.set_Dropoff_Cell_Blocks()

    def set_State_Environment(self):
        self.environment = self.world_environment.environment

    def set_Male_Position(self):
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    if self.environment[x][y][z]['occupied_by'] == 'm':
                        self.representation['male_position']['coords'] = [x, y, z]
                        self.representation['male_position']['cell_type'] = self.environment[x][y][z]['type']

    def set_Female_Position(self):
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    if self.environment[x][y][z]['occupied_by'] == 'f':
                        self.representation['female_position']['coords'] = [x, y, z]
                        self.representation['female_position']['cell_type'] = self.environment[x][y][z]['type']

    def toggle_Male_Carrying(self):
        self.representation['male_carrying'] = not self.representation['male_carrying']

    def toggle_Female_Carrying(self):
        self.representation['female_carrying'] = not self.representation['female_carrying']

    def set_Pickup_Cell_Blocks(self):
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    if self.environment[x][y][z]['type'] == 'pickup':
                        self.representation['pickup_cell_blocks'][(x, y, z)] = self.environment[x][y][z]['block_count']

    def set_Dropoff_Cell_Blocks(self):
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    if self.environment[x][y][z]['type'] == 'dropoff':
                        self.representation['dropoff_cell_blocks'][(x, y, z)] = self.environment[x][y][z]['block_count']

    def update_Environment_And_State(self, old_coords, action, agent, carrying, new_position):
        self.world_environment.move_agent(old_coords, action, agent, carrying)
        if agent == 'm':
            self.set_Male_Position()
        else:
            self.set_Female_Position()
        if (new_position == 'dropoff' and carrying) or (new_position == 'pickup' and carrying == False):
            if agent == 'm':
                self.toggle_Male_Carrying()
            else:
                self.toggle_Female_Carrying()
        if new_position == 'dropoff' and carrying:
            self.set_Dropoff_Cell_Blocks()
        elif new_position == 'pickup' and carrying == False:
            self.set_Pickup_Cell_Blocks()
        self.set_State_Environment()


def find_Possible_Cells(state, agent, actions):
    possible_cells = {}
    if agent == 'm':
        possible_cells = environment.get_Cell_Types(state.environment, state.representation['male_position']['coords'],
                                                    actions)
    else:
        possible_cells = environment.get_Cell_Types(state.environment,
                                                    state.representation['female_position']['coords'], actions)
    return possible_cells


def find_Next_Position_Possible_Cells(state, coords, actions):
    possible_cells = environment.get_Cell_Types(state.environment, coords, actions)
    return possible_cells
