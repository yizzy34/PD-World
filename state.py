import environment


class State:
    def __init__(self, world_environment):
        self.world_environment = world_environment
        self.representation = {'male_position': {}, 'female_position': {}, 'male_carrying': False,
                               'female_carrying': False, 'pickup_cell_blocks': {}, 'dropoff_cell_blocks': {}}
        self.set_state_environment()
        self.set_male_position()
        self.set_female_position()
        self.set_pickup_cell_blocks()
        self.set_dropoff_cell_blocks()

    def set_state_environment(self):
        self.environment = self.world_environment.environment

    def set_male_position(self):
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    if self.environment[x][y][z]['occupied_by'] == 'm':
                        self.representation['male_position']['coords'] = [x, y, z]
                        self.representation['male_position']['cell_type'] = self.environment[x][y][z]['type']

    def set_female_position(self):
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    if self.environment[x][y][z]['occupied_by'] == 'f':
                        self.representation['female_position']['coords'] = [x, y, z]
                        self.representation['female_position']['cell_type'] = self.environment[x][y][z]['type']

    def toggle_male_carrying(self):
        self.representation['male_carrying'] = not self.representation['male_carrying']

    def toggle_female_carrying(self):
        self.representation['female_carrying'] = not self.representation['female_carrying']

    def set_pickup_cell_blocks(self):
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    if self.environment[x][y][z]['type'] == 'pickup':
                        self.representation['pickup_cell_blocks'][(x, y, z)] = self.environment[x][y][z]['block_count']

    def set_dropoff_cell_blocks(self):
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    if self.environment[x][y][z]['type'] == 'dropoff':
                        self.representation['dropoff_cell_blocks'][(x, y, z)] = self.environment[x][y][z]['block_count']

    def update_environment_and_state(self, old_coords, action, agent, carrying, new_position):
        picked_up_or_dropped_off = self.world_environment.move_agent(old_coords, action, agent, carrying)
        if agent == 'm':
            self.set_male_position()
        else:
            self.set_female_position()
        if picked_up_or_dropped_off:
            if new_position == 'pickup' and carrying == False:
                self.set_pickup_cell_blocks()
            else:
                self.set_dropoff_cell_blocks()
            if agent == 'm':
                self.toggle_male_carrying
            else:
                self.toggle_female_carrying
        self.set_state_environment()
        return picked_up_or_dropped_off


def find_possible_cells(state, agent, actions):
    possible_cells = {}
    if agent == 'm':
        possible_cells = environment.get_cell_types(state.environment, state.representation['male_position']['coords'],
                                                    actions)
    else:
        possible_cells = environment.get_cell_types(state.environment,
                                                    state.representation['female_position']['coords'], actions)
    return possible_cells


def find_next_position_possible_cells(state, coords, actions):
    possible_cells = environment.get_cell_types(state.environment, coords, actions)
    return possible_cells
